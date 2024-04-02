from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from time import sleep
import asyncio
import json
from channels.db import database_sync_to_async

from .models import Chats,Group

class MySyncConsumer(SyncConsumer):
    # websocket.connect message is handled by websocket_connect 
    def websocket_connect(self,event):
        print('websocket connected...')
        # print('Channel_Name..',self.channel_name)
        # add a channel to new or existing group
        # this asynch method == self.channel_layer.group_add('programmers',self.channel_name)
        # print(self.scope['url_route']['kwargs']['groupname'])
        groupName=self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_add)(groupName,self.channel_name)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        print('websocket received...')
        # type :websocket.receive
        # bytes: The message content if it was binary mode 
        # text: The message content if it was text mode
        # print('event...',event)
        # print(groupName)
        groupName=self.scope['url_route']['kwargs']['groupname']
        data=json.loads(event['text'])
        # print(data['msg'])
        group=Group.objects.get(name=groupName)
        chat=Chats(group=group,content=data['msg'])
        chat.save()        
        async_to_sync(self.channel_layer.group_send)(groupName,{
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
        groupName=self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_discard)(groupName,self.channel_name)
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connected...')
        groupName=self.scope['url_route']['kwargs']['groupname']
        await self.channel_layer.group_add(groupName,self.channel_name)
        await self.send({
            'type':'websocket.accept',
        })
    
    async def websocket_receive(self,event):
        print('websocket received...')
        # print('event..',event)
        groupName=self.scope['url_route']['kwargs']['groupname']
        data=json.loads(event['text'])
        # print(data['msg'])
        group=await database_sync_to_async(Group.objects.get)(name=groupName)
        chat=Chats(group=group,content=data['msg'])
        await database_sync_to_async(chat.save)()   
        await self.channel_layer.group_send(groupName,{
            'type':'chat.message',
            'message':event['text']
        })

    async def chat_message(self,event):
        # print('chat..event',event)
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })
    
    async def websocket_disconnect(self,event):
        groupName=self.scope['url_route']['kwargs']['groupname']
        await self.channel_layer.group_discard(groupName,self.channel_name)
        raise StopConsumer()
