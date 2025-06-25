from tkinter.constants import RAISED # not useful

from loguru import logger


SOCKETS = {} # global dict to simulate active ports and running servers, key is number of port, value is instance Server which runs on that port

class Server:
    def __init__(self, port=80):
        self.port = port # port the server will run on, value is 80 if not defined
        self.status = False # server running status

    def start(self): # method for running the server
        if self.port and not self.status: # only start if port is set and server is stopped (self.status == False)
            if SOCKETS.get(self.port): # checks if port is already in use
                raise Exception(f'Port {self.port} unavailable')
            SOCKETS[self.port] = self # add this server to Sockets so it registers on the port
            self.status = True # mark server as running
            logger.info(f"server started {self.port}") # log start message
        else:
            raise Exception("Server start error") # raise error if already running or invalid

    def stop(self): # method to stop server
        if self.status: # only stop if server is running
            logger.info(f"server stopping") # log stop message
            del SOCKETS[self.port] # remove server from global ports (sockets) 'free the port'
            self.status = False # mark server as stopped
        else:
            raise Exception("Server stop error") # raise error if already stopped


    def send(self, message): # simulates sending the message via server, only if server is running (status == True)
        if self.status:
            return f"Server: {message}" # simulate server response
        return None # return nothing if server is not running



class Client: # client who connects to server
    def __init__(self, port):
        self.port = port # port client will connect to

    def send(self, message):
        if self.port: # check if port is set
            server = SOCKETS.get(self.port) # get server from global port map

            if server: # if server exists
                response = server.send(message) # send message to server
                logger.info(f"Sending message {message}") # log message
                return response # return server's response
            else:
                raise Exception("Cannot connect to server") # no server found
        else:
            raise Exception("No port defined") # port not specified
