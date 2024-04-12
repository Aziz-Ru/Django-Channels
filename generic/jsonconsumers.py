from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer
from time import sleep
from asgiref.sync import async_to_sync
import asyncio
from .models import Group,Chat
from channels.db import database_sync_to_async
class MyjsonWebsocketConsumers(JsonWebsocketConsumer):
    def connect(self):
        print('websocket connected...')
        self.accept()
        self.group_name=self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
    
    def receive_json(self, content, **kwargs):
        print('message received...')
        # print('Content...',content)
        # print('Type of Content...',type(content)) # python dictionay
        # for i in range(10):
        #     self.send_json({'message':i})
        #     sleep(1)
        group_name=Group.objects.get(name=self.group_name)
        # print(content['message'])
        chat=Chat(group=group_name,content=content['msg'])
        chat.save()
        # self.send_json({'msg':content['msg']})
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,{
                'type':'chat.message',
                'message':content['msg']
            }
        )
    def chat_message(self,event):
        self.send_json({'msg':event['message']})

            
        
    def disconnect(self, code):
        print('Disconnect...')


class MyAsyncjsonWebsocketConsumers(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print('websocket connected...')
        await self.accept()
        self.group_name=self.scope['url_route']['kwargs']['groupname']
        await self.channel_layer.group_add(self.group_name,self.channel_name)
    
    async def receive_json(self, content, **kwargs):
        print('message received...')
        # print('Content...',content)
        # print('Type of Content...',type(content)) # python dictionay
        # await self.send_json(content=content)
        # for i in range(10):
        #     await self.send_json({'message':i})
        #     await asyncio.sleep(1)
        group_name=await database_sync_to_async(Group.objects.get)(name=self.group_name)
        # print(content['message'])
        chat=Chat(group=group_name,content=content['msg'])
        await database_sync_to_async(chat.save)()
        # self.send_json({'msg':content['msg']})
        await self.channel_layer.group_send(
            self.group_name,{
                'type':'chat.message',
                'message':content['msg']
            }
        )
    async def chat_message(self,event):
        await self.send_json({'msg':event['message']})
        
    async def disconnect(self, code):
        print('Disconnect...')


