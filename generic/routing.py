from django.urls import path
from .consumers import MySyncWebsocketConsumer,MyAsyncWebsocketConsumer
from .jsonconsumers import MyjsonWebsocketConsumers,MyAsyncjsonWebsocketConsumers
generic_websocket_consumers_urlpatterns=[
    path('generic/sc/<str:groupname>/',MySyncWebsocketConsumer.as_asgi()),
    path('generic/ac/<str:groupname>/',MyAsyncWebsocketConsumer.as_asgi()),
    path('json/sc/<str:groupname>/',MyjsonWebsocketConsumers.as_asgi()),
    path('json/ac/<str:groupname>/',MyAsyncjsonWebsocketConsumers.as_asgi()),
]
