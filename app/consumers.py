from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connected...')
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        print('websocket received...')
        print('client msg:',event['text'])
    
    def websocket_disconnect(self,event):
        print('websocket disconnted...')

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connected...')
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self,event):
        print('websocket received...')
        print('client msg:',event['text'])
    
    async def websocket_disconnect(self,event):
        print('websocket disconnted...')
