
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
from asgiref.sync import async_to_sync,sync_to_async
import asyncio
import json
from .models import Chat,Group
from channels.db import database_sync_to_async

class MySyncWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print('Websocket Connected')
        self.accept() #to accept the connection
        # self.close() # to reject the connection
        # print("Channel Layer...",self.channel_layer)
        # print('CHannel Name...',self.channel_name)
        self.group_name=self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        # print(self.group_name)
    def receive(self, text_data=None, bytes_data=None):
        print('Data received ')
        # print('Data>>',text_data)
        data=json.loads(text_data)
        message=data['msg']
        # print(message)
        # self.close(code=4123)
        group_name=Group.objects.get(name=self.group_name)
        chat=Chat(group=group_name,content=message)
        chat.save()
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,{
                'type':'chat.message',
                'message':message
            }
        )
    def chat_message(self,event):
        # print(event)
        self.send(text_data=json.dumps({'msg':event['message']}))

    
    def disconnect(self, code):
        print('Disconnected')

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('Websocket Connected')
        await self.accept() #to accept the connection
        # self.close() # to reject the connection
        self.group_name=self.scope['url_route']['kwargs']['groupname']
        await self.channel_layer.group_add(self.group_name,self.channel_name)
    
    async def receive(self, text_data=None, bytes_data=None):
        print('Data received ')
        # await self.send(text_data=text_data)
        data=json.loads(text_data)
        message=data['msg']

        group_name=await database_sync_to_async(Group.objects.get)(name=self.group_name)
        chat=Chat(group=group_name,content=message)
        await database_sync_to_async(chat.save)()
        
        await self.channel_layer.group_send(
            self.group_name,{
                'type':'chat.message',
                'message':message
            }
        )
    async def chat_message(self,event):
        # print(event)
        await self.send(text_data=json.dumps({'msg':event['message']}))
        # await self.close(code=4123)
    
    async def disconnect(self, code):
        print('Disconnected')