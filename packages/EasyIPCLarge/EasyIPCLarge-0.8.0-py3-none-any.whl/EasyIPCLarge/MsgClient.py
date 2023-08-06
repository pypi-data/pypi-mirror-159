from EasyIPCLarge.Msg import Msg
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from typing import Dict
import json


class MsgClient:
    def __init__(self,
                 port:  int):
        sock = TSocket.TSocket("127.0.0.1", port)
        self.__transport = TTransport.TFramedTransport(sock)
        protocol = TBinaryProtocol.TBinaryProtocol(self.__transport)
        self.__client = Msg.Client(protocol)
        self.__transport.open()

    def Req(self,
            req: Dict
            ) -> Dict:
        return json.loads(self.__client.Send(json.dumps(req)))

    def __del__(self):
        self.__transport.close()


if __name__ == "__main__":
    m = MsgClient(8000)
