from django.urls import path
from .consumers import MySyncConsumer,MyAsyncConsumer

websocket_urlpatterns=[
    path('sc/',MySyncConsumer.as_asgi()),
    path('ac/',MyAsyncConsumer.as_asgi()),
]
