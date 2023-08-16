from django.urls import path
from . import views
from .consumers import ChatConsumer

urlpatterns = [
    path('message/<str:username>/', views.SendMessageView.as_view(), name='message'),
    # path('send_message/', views.MessagePageView.as_view(), name='send_message'),
    path('chat/<str:username>/', views.chat_with_user, name='chat_with_user'),
]


websocket_urlpatterns = [  
    path('ws/chat/',  ChatConsumer.as_asgi())
]




