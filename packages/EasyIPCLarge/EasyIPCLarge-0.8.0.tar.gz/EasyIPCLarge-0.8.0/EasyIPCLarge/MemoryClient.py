from EasyIPCLarge.MsgClient import MsgClient
from EasyIPCLarge.NameConst import NameConst as nc
from multiprocessing import shared_memory
from threading import Thread
from typing import Dict
import uuid
import threading
import time


class MemoryClient:
    def __init__(self,
                 port: int):
        self.__msgClient = MsgClient(port)
        self.__sessionID = str(uuid.uuid4())
        self.__running = False
        self.__memory = None
        self.__memorySize = 0
        self.__memoryIndexR = 0
        self.__memoryIndexW = 0
        self.__memoryBlocks = []
        self.__memoryThread = None
        self.__gCond = threading.Condition()

    def __del__(self):
        self.__CleanShareMemory()

    def __PrepareShareMemory(self, size: int):
        self.__CleanShareMemory()
        self.__memory = shared_memory.SharedMemory(create=True, size=size)
        self.__memorySize = size
        self.__memoryIndexR = 0
        self.__memoryIndexW = 0

    def __CleanShareMemory(self):
        if self.__memory is not None:
            self.__memory.close()
            self.__memory.unlink()
            self.__memory = None

    def SharedMemoryOpen(self, memorySize: int):
        self.__PrepareShareMemory(memorySize)

        req = {}
        req[nc.kSessionID] = self.__sessionID
        req[nc.kAction] = nc.vOpen
        req[nc.kSharedMemoryName] = self.__memory.name
        self.__msgClient.Req(req)

        self.__memoryThread = Thread(target=self.__SharedMemoryNotify)
        self.__memoryThread.start()

    def SharedMemoryClose(self):
        self.__running = False
        self.__gCond.acquire()
        self.__gCond.notifyAll()
        self.__gCond.release()
        if self.__memoryThread:
            self.__memoryThread.join()
            self.__memoryThread = None

        req = {}
        req[nc.kSessionID] = self.__sessionID
        req[nc.kAction] = nc.vClose
        self.__msgClient.Req(req)

        self.__CleanShareMemory()

    def SharedMemorySend(self,
                         seq: int,
                         data: bytes,
                         timeout: float = 1.0) -> bool:
        ret = False
        sz = len(data)
        t0 = time.time_ns() // 1000

        self.__gCond.acquire()

        ind = self.__SharedMemoryRequireSpace(sz)
        if ind < 0:
            self.__gCond.wait(timeout)
            ind = self.__SharedMemoryRequireSpace(sz)

        if ind >= 0:
            self.__memory.buf[ind:ind+sz] = data[:]
            self.__memoryIndexW += sz
            self.__memoryBlocks.append([ind, sz, seq, t0])
            self.__gCond.notifyAll()
            ret = True

        self.__gCond.release()

        return ret

    def SharedMemoryEmpty(self) -> bool:
        return len(self.__memoryBlocks) == 0

    def ExternalReq(self, req: Dict) -> Dict:
        reqTpl = {}
        reqTpl[nc.kSessionID] = self.__sessionID
        reqTpl[nc.kAction] = nc.vExternal
        reqTpl[nc.kTime] = str(time.time_ns() // 1000)
        reqTpl[nc.kBody] = req
        respTpl = self.__msgClient.Req(reqTpl)
        return respTpl[nc.kBody]

    def __SharedMemoryRequireSpace(self, sz: int) -> int:
        indR = self.__memoryIndexR
        indW = self.__memoryIndexW
        if indW >= indR:
            if indW + sz < self.__memorySize:
                return indW
            else:
                if sz < indR:  # rewind
                    self.__memoryIndexW = 0
                    return 0
                else:
                    return -1
        else:
            if indR - indW > sz:
                return indW
            else:
                return -1

    def __SharedMemoryNotify(self):
        self.__running = True
        wTimeLong = 0.1
        wTimeShort = 0.002

        while self.__running:
            self.__gCond.acquire()
            while self.__running and len(self.__memoryBlocks) == 0:
                self.__gCond.wait(wTimeLong)
            self.__gCond.release()

            if not self.__running:
                break

            info = self.__memoryBlocks[0]
            ind = info[0]
            sz = info[1]
            seq = info[2]
            t0 = info[3]
            req = {}
            req[nc.kSessionID] = self.__sessionID
            req[nc.kAction] = nc.vSend
            req[nc.kRange] = "{}-{}".format(ind, ind + sz)
            req[nc.kSeq] = str(seq)
            req[nc.kTime] = str(t0)

            while self.__running:
                resp = self.__msgClient.Req(req)
                if resp[nc.kErr] == nc.vErrOK:
                    self.__memoryIndexR = (ind + sz) % self.__memorySize
                    self.__memoryBlocks.pop(0)
                    self.__gCond.acquire()
                    self.__gCond.notifyAll()
                    self.__gCond.release()
                    break
                time.sleep(wTimeShort)
