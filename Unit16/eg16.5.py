from SocketServer import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST = ''
PORT = 21528
ADDR = (HOST, PORT)


class MyServerHandler(SRH):
    def handle(self):
        print '... connected from  ', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))


tcpServer = TCP(ADDR, MyServerHandler)
print '...waiting ', tcpServer.server_address
tcpServer.serve_forever()
