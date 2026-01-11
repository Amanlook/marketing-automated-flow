import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chatgames.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketing_automation.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chatgames.routing.websocket_urlpatterns
        )
    ),
})