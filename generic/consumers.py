
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
import asyncio

class MySyncWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print('Websocket Connected')
        self.accept() #to accept the connection
        # self.close() # to reject the connection
        # print("Channel Layer...",self.channel_layer)
        # print('CHannel Name...',self.channel_name)
        self.group_name=self.scope['']
    
    def receive(self, text_data=None, bytes_data=None):
        print('Data received ')
        print('Data>>',text_data)
        for i in range(20):
            self.send(text_data=str(i))
            sleep(1)
        # self.close(code=4123)
    
    def disconnect(self, code):
        print('Disconnected')

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('Websocket Connected')
        await self.accept() #to accept the connection
        # self.close() # to reject the connection
    
    async def receive(self, text_data=None, bytes_data=None):
        print('Data received ')
        # await self.send(text_data=text_data)
        print('Data>>',text_data)
        for i in range(20):
            await self.send(text_data=str(i+1))
            await asyncio.sleep(1)
        # await self.close(code=4123)
    
    async def disconnect(self, code):
        print('Disconnected')