from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from channels.routing import ProtocolTypeRouter, URLRouter
from messages_between_users.routing import websocket_urlpatterns  
from django.core.asgi import get_asgi_application
from django.urls import re_path
from messages_between_users import consumers



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('messages_between_users.urls')),
    path('', include('meeting_create_user.urls')),
    path('', include('messages_between_users.routing')),
]

websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),
]

# Подключаем маршрутизатор для WebSocket-каналов
application = ProtocolTypeRouter({
    'ws': get_asgi_application(),  # Обработка HTTP-запросов
    'websocket': URLRouter(websocket_urlpatterns),  # Обработка WebSocket-запросов
})


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
