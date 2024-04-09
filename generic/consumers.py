
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer

class MySyncWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print('Websocket Connected')
        self.accept() #to accept the connection
        # self.close() # to reject the connection
    
    def receive(self, text_data=None, bytes_data=None):
        print('Data received ')
        self.send(text_data=text_data)
        print('Data>>',text_data)
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
        await self.send(text_data=text_data)
        print('Data>>',text_data)
        # await self.close(code=4123)
    
    async def disconnect(self, code):
        print('Disconnected')