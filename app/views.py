from django.shortcuts import render
from .models import*
# channel layer allows you to talk between different instance of an application
# a channel layer is the transport mechanism that allows multiple consumer instance to communicate
# with each other
# Redis channel layer---production
# In memory chanel layer---for development
def index(request,group_name):
    # print(group_name)
    group=Group.objects.filter(name=group_name).first()
    chats=[]
    if group:
        chats=Chats.objects.filter(group=group)
    else :
        group=Group(name=group_name)
        group.save() 
    return render(request,'app/index.html',{'group':group_name,'chats':chats})



'''
get_channel_layer()=this function is used to get default channnel layer from project.
from channels.layers import get_channel_layer
channel_layer= this attributeis used to get default channel layer from a project.
channel_name=this attribute contains the channel name that will reach the consumer.
send()==send('channel_name',message)
group_send()==group_send('group_channel_name',message)
 
'''
