
import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from app.routing import websocket_urlpatterns
from generic.routing import generic_websocket_consumers_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CHANNEL.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(generic_websocket_consumers_urlpatterns)

})
