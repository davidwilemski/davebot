from tornado import ioloop
from tornado import iostream
from tornado import netutil
import socket

class MyTCPServer(netutil.TCPServer):
    def handle_stream(self, stream, address):
        MyTCPConnection(stream, address)


class MyTCPConnection(object):
    """Handles the TCP connection"""
    def __init__(self, stream, address):
        self.stream = stream
        self.address = address

        self.stream.read_until_close(lambda x: 'done', self.streaming_callback)

    def streaming_callback(self, data):
        data = data.rstrip()
        print 'data: ' + data

        if data == 'hi':
            self.stream.write('bye\n')
        elif data == 'bye':
            self.stream.write('That\'s my line!\n')
        elif data == 'blah':
            self.stream.write('I\'m bored too!\n')
        else:
            self.stream.write('Sorry, I don\'t recognize that.\n')

if __name__ == '__main__':
    server = MyTCPServer()
    server.listen(8888)
    ioloop.IOLoop.instance().start()
