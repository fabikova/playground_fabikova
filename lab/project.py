from tkinter.constants import RAISED

from loguru import logger


SOCKETS = {}

class Server:
    def __init__(self, port=80):
        self.port = port
        self.status = False

    def start(self):
        if self.port and not self.status:
            if SOCKETS.get(self.port):
                raise Exception(f'Port {self.port} unavailable')
            SOCKETS[self.port] = self
            self.status = True
            logger.info(f"server started {self.port}")
        else:
            raise Exception("Server start error")

    def stop(self):
        if self.status:
            logger.info(f"server stopping")
            del SOCKETS[self.port]
            self.status = False
        else:
            raise Exception("Server stop error")


    def send(self, message):
        if self.status:
            return f"Server: {message}"
        return None



class Client:
    def __init__(self, port):
        self.port = port

    def send(self, message):
        if self.port:
            server = SOCKETS.get(self.port)

            if server:
                response = server.send(message)
                logger.info(f"Sending message {message}")
                return response
            else:
                raise Exception("Cannot connect to server")
        else:
            raise Exception("No port defined")
