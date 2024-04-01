from django.shortcuts import render

# channel layer allows you to talk between different instance of an application
# a channel layer is the transport mechanism that allows multiple consumer instance to communicate
# with each other
# Redis channel layer---production
# In memory chanel layer---for development
def index(request,group_name):
    # print(group_name)
    return render(request,'app/index.html',{'group':group_name})



'''
get_channel_layer()=this function is used to get default channnel layer from project.
from channels.layers import get_channel_layer
channel_layer= this attributeis used to get default channel layer from a project.
channel_name=this attribute contains the channel name that will reach the consumer.
send()==send('channel_name',message)
group_send()==group_send('group_channel_name',message)
 
'''
