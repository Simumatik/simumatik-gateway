import logging
import json
import enum 

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class GatewayWsCommands(str, ):
    CONNECT = 'connect'
    DISCONNECT = 'disconnect'
    RESET = 'reset'
    STATUS = 'status'
    UNKNOWN = 'unknown'
    VERSION = "version"


class GatewayWsInterfaceClient(WebSocket):
    
    def sendCommand(self, command:GatewayWsCommands, data:dict) -> dict:
        self.server._pipe.send((command, data))
        return self.server._pipe.recv()

    def handleMessage(self):
        if self.server._actual_connection == self:
            try:
                msg = json.loads(self.data)
                assert 'request' in msg
                self.server._logger.debug(f'GatewayWsInterface: Message received from {self.address} -> {msg}')
                req = msg['request']
                (command, resp_data) = self.sendCommand(command=req.get('command', GatewayWsCommands.UNKNOWN), data=req.get('data', {}))
                response = json.dumps({"response": {"id": req.get("id", 0), "command": command, "data": resp_data}})
                self.sendMessage(response)
                self.server._logger.debug(f'GatewayWsInterface: Message response sent to {self.address} -> {response}')
            except:
                self.server._logger.error(f'GatewayWsInterface: Message received has wrong format {self.address} -> {self.data}')
        
    def handleConnected(self):
        if self.server._actual_connection is not None:
            self.server._logger.info(f'GatewayWsInterface: New connection request, disconnecting previous connection from {self.server._actual_connection.address}')
            self.server._actual_connection.close()
        self.server._actual_connection = self
        self.server._logger.info(f'GatewayWsInterface: Connected to {self.address}')
            

    def handleClose(self):
        if self.server._actual_connection == self:
            self.server._logger.info(f'GatewayWsInterface: Disconnected from {self.address}')
            self.server._actual_connection = None

# WebSocket Thread method
def GatewayWsInterface(ip:str, port:int, pipe:any, log_level:int=logging.ERROR):
    server = SimpleWebSocketServer(ip, port, GatewayWsInterfaceClient)
    server._pipe = pipe
    server._actual_connection = None
    server._logger = logging.getLogger('GatewayWSInterface')
    server._logger.setLevel(log_level)
    if not server._logger.handlers: server._logger.addHandler(logging.StreamHandler())
    server.serveforever()