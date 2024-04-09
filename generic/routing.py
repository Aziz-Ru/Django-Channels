from django.urls import path
from .consumers import MySyncWebsocketConsumer,MyAsyncWebsocketConsumer

generic_websocket_consumers_urlpatterns=[
    path('generic/sc/',MySyncWebsocketConsumer.as_asgi()),
    path('generic/ac/',MyAsyncWebsocketConsumer.as_asgi()),
]
