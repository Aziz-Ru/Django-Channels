from django.urls import path
from .consumers import MySyncWebsocketConsumer,MyAsyncWebsocketConsumer

generic_websocket_consumers_urlpatterns=[
    path('generic/sc/<str:groupname>/',MySyncWebsocketConsumer.as_asgi()),
    path('generic/ac/<str:groupname>/',MyAsyncWebsocketConsumer.as_asgi()),
]
