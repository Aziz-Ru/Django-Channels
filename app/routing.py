from django.urls import path
from .consumers import MySyncConsumer,MyAsyncConsumer

websocket_urlpatterns=[
    path('sc/<str:groupname>/',MySyncConsumer.as_asgi()),
    path('ac/<str:groupname>/',MyAsyncConsumer.as_asgi()),
]
