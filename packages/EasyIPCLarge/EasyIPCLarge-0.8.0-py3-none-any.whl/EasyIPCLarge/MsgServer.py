from EasyIPCLarge.Msg import Msg
from thrift.transport import TSocket
from thrift.server import TNonblockingServer
from threading import Thread
from typing import Callable, Dict
import time
import json


class MsgHandler:
    def __init__(self,
                 OnReq: Callable[[Dict], Dict] = None):
        self.__OnReq = OnReq

    def Send(self, req):
        if self.__OnReq:
            return json.dumps(self.__OnReq(json.loads(req)))
        else:
            return json.dumps({})


class MsgServer:
    def __init__(self,
                 port:  int,
                 OnReq: Callable[[Dict], Dict] = None):
        handler = MsgHandler(OnReq)
        processor = Msg.Processor(handler)
        transport = TSocket.TServerSocket("127.0.0.1", port)
        self.__server = TNonblockingServer.TNonblockingServer(processor,
                                                              transport)
        self.__t = Thread(target=self.__Loop)
        self.__t.start()

    def __Loop(self):
        self.__server.serve()

    def Stop(self):
        if self.__t:
            self.__server.stop()
            self.__t.join()


if __name__ == "__main__":
    server = MsgServer(8000)
    time.sleep(24*3600)
    server.Stop()
