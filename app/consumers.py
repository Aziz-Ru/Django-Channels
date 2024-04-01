from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from time import sleep
import asyncio
import json

class MySyncConsumer(SyncConsumer):
    # websocket.connect message is handled by websocket_connect 
    def websocket_connect(self,event):
        print('websocket connected...')
        # print('Channel_Name..',self.channel_name)
        # add a channel to new or existing group
        # this asynch method == self.channel_layer.group_add('programmers',self.channel_name)
        async_to_sync(self.channel_layer.group_add)('programmers',self.channel_name)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        print('websocket received...')
        # type :websocket.receive
        # bytes: The message content if it was binary mode 
        # text: The message content if it was text mode
        # print('event...',event)
        async_to_sync(self.channel_layer.group_send)('programmers',{
            'type':'chat.message',
            'message':event['text']
        })
            
    def chat_message(self,event):
        # print('chat..event',event)
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })
        
    
    def websocket_disconnect(self,event):
        async_to_sync(self.channel_layer.group_discard)('programmers',self.channel_name)
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
