from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json

class MySyncConsumer(SyncConsumer):
    # websocket.connect message is handled by websocket_connect 
    def websocket_connect(self,event):
        print('websocket connected...')
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        print('websocket received...')
        # type :websocket.receive
        # bytes: The message content if it was binary mode 
        # text: The message content if it was text mode
        for i in range(10):
            self.send({
            'type':'websocket.send',
            'text':json.dumps({'cnt':str(i)})
            })
            sleep(1)
    
    def websocket_disconnect(self,event):
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connected...')
        await self.send({
            'type':'websocket.accept',
        })
    
    async def websocket_receive(self,event):
        print('websocket received...')
        for i in range(10):
            await self.send({
            'type':'websocket.send',
            'text':str(i)
            })
            await asyncio.sleep(1)
    
    async def websocket_disconnect(self,event):
        raise StopConsumer()
