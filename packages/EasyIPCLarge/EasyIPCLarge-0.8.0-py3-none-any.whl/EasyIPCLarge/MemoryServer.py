from EasyIPCLarge.MsgServer import MsgServer
from EasyIPCLarge.NameConst import NameConst as nc
from multiprocessing import shared_memory
from typing import Callable, Dict, Tuple
import threading
import time


class DataSession:
    def __init__(self, sessionID: str, sharedMemoryName: str):
        self.__sessionID = sessionID
        self.__sharedMemoryName = sharedMemoryName
        self.__memory = shared_memory.SharedMemory(name=sharedMemoryName)

    def __del__(self):
        if self.__memory:
            self.__memory.close()

    @property
    def memory(self):
        return self.__memory


class MemoryServer:
    def __init__(self,
                 port: int,
                 memoryLimit: int = 32*1024*1024,
                 onExternalReq: Callable[[int, Dict], Dict] = None):
        self.__msgServer = MsgServer(port, OnReq=self.__OnReq)
        self.__onExternalReq = onExternalReq
        self.__sessions = {}
        self.__seqNext = 0
        self.__blocks = []
        self.__memoryFreeBytes = memoryLimit
        self.__gCond = threading.Condition()

    def Stop(self):
        self.__gCond.acquire()
        self.__gCond.notifyAll()
        self.__gCond.release()
        if self.__msgServer:
            self.__msgServer.Stop()

    def NoSessions(self) -> bool:
        return len(self.__sessions) == 0

    def GetData(self, timeout: float = 1.0) -> Tuple[int, bytes]:
        seq, b = -1, None
        tCreate = None

        self.__gCond.acquire()
        if len(self.__blocks) == 0 or self.__blocks[0][0] != self.__seqNext:
            self.__gCond.wait(timeout)
        if len(self.__blocks) != 0 and self.__blocks[0][0] == self.__seqNext:
            block = self.__blocks.pop(0)
            seq = block[0]
            tCreate = block[1]
            b = block[2]
            self.__seqNext += 1
            self.__memoryFreeBytes += len(b)
        self.__gCond.release()

        delayUS = 0 if tCreate is None else time.time_ns() // 1000 - tCreate
        return seq, delayUS, b

    def __OnReq(self, req: Dict) -> Dict:
        resp = {}
        resp[nc.kErr] = nc.vErrOK

        sessionID = req.get(nc.kSessionID)
        action = req.get(nc.kAction)

        if action == nc.vOpen:
            sharedMemoryName = req.get(nc.kSharedMemoryName)
            self.__sessions[sessionID] = DataSession(sessionID,
                                                     sharedMemoryName)
        elif action == nc.vClose:
            session = self.__sessions.pop(sessionID)
            del session
        elif action == nc.vSend:
            session = self.__sessions.get(sessionID)
            if session and session.memory:
                seq = int(req[nc.kSeq])
                timeCreate = int(req[nc.kTime])
                ranges = req[nc.kRange].split("-")
                indL = int(ranges[0])
                indR = int(ranges[1])
                if not self.__BlockInsert(seq, timeCreate, session.memory.buf,
                                          indL, indR):
                    resp[nc.kErr] = nc.vErrNoMemory
        elif action == nc.vExternal:
            t0 = int(req[nc.kTime])
            delayUS = time.time_ns() // 1000 - t0
            if self.__onExternalReq:
                resp[nc.kBody] = self.__onExternalReq(delayUS, req[nc.kBody])

        return resp

    def __BlockInsert(self, seq: int, timeCreate: int,
                      buf: bytes, indL: int, indR: int) -> bool:
        if (self.__memoryFreeBytes < indR - indL) and (seq != self.__seqNext):
            return False

        b = bytes(buf[indL:indR])
        self.__gCond.acquire()
        self.__blocks.append([seq, timeCreate, b])
        self.__memoryFreeBytes -= len(b)
        self.__blocks.sort(key=lambda x: x[0])
        self.__gCond.notifyAll()
        self.__gCond.release()

        return True
