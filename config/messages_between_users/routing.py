from django.urls import path, re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from .consumers import ChatConsumer
from . import views


urlpatterns = [
    path('message/<str:username>/', views.SendMessageView.as_view(), name='message'),
   
]


websocket_urlpatterns = [  path('ws/chat/<str:username>/',  ChatConsumer.as_asgi())]




# Протоколы и соответствующие middleware для обработки WebSocket-запросов
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
