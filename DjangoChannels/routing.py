from channels.routing import ProtocalTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import myapp.routing

application = ProtocalTypeRouter({
   'websocket': AuthMiddlewareStack(
       URLRouter(
           myapp.routing.websocket_urlpatterns
       )
   ),
})