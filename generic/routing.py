from django.urls import path
from .consumers import MySyncConsumer,MyAsyncConsumer

generic_websocket_consumers_urlpatterns=[
    path('generic/sc/<str:groupname>/',MySyncConsumer.as_asgi()),
    path('generic/ac/<str:groupname>/',MyAsyncConsumer.as_asgi()),
]
