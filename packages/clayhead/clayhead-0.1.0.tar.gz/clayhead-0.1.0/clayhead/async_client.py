from typing import Dict

import socketio


class AsyncCharacterController:

    def __init__(self, socket, characterKey):
        self._sio = socket
        self.characterKey = characterKey
        self.id = None

    async def initialize(self):
        self.id = await self._sio.emit("create", self.characterKey)



class AsyncClayheadClient:
    
    def __init__(self, url: str, options: Dict):
        self._sio = socketio.AsyncClient()

    def controller(self, characterKey: str) -> AsyncCharacterController:
        return AsyncCharacterController(self._sio, characterKey)

    
    