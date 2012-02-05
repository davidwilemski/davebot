
from tornado import ioloop, iostream, netutil
import socket


class Adapter(object):
    """
    Base connection adapter, must be extended to do anything

    Instantiating an implementation ofthis class automatically 
    starts the IOLoop instance and calls the run() function. 

    run() is the function that must be overridden in a subclass
    """
    def __init__(self, host, port, greet=True):
        self.host = host
        self.port = port
        self.greet = greet
        stream = self.build_connection(host, port)
        self.stream = stream

    def start(self):
        """
        starts the adapter by connecting the stream and 
        runs the IOLoop
        """
        self.stream.connect((self.host, self.port), self.run)
        ioloop.IOLoop.instance().start()

    def stop(self):
        """
        method to close the connection and stop the ioloop
        """
        self.stream.close()
        ioloop.IOLoop.instance().stop()

    def build_connection(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        stream = iostream.IOStream(s)
        return stream

    def bot(self, data):
        """
        This method will do processing on messages recieved through the
        server (irc channel) and react accordingly

        Hopefully it will also be modularized so that it is easy to write
        simple scripts to extend davebot
        """
        data = data.rstrip()
        print data

        if data.rstrip() == 'bye':
            self.stream.write('goodbye!')

class TextAdapter(Adapter):
    """
    This is a basic adapter for a pure text network protocol.

    This can be used for testing however there will need to be work
    on the irc adapter. These adapters may also be able to be modular
    """
    def run(self):
        
        if self.greet:
            self.stream.write('hi') # greet the server when connected
    
        # The lambda function is there simply as a place holder.
        # At this point it doesn't matter what we do after the connection.
        self.stream.read_until_close(lambda x: 'nothin', self.bot) # react to data

if __name__ == '__main__':
    t = TextAdapter('localhost', 8888)
    t.start()
