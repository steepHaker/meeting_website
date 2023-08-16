# users/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

# import django

# django.setup()

from .models import User
from .models import Messages

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['username']

        self.room_group_name = f'chat_{self.room_name}'

        # Присоединяемся к комнате с именем пользователя
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Отсоединяемся от комнаты с именем пользователя
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['messagetext']
        user = self.scope['user']
        recipient_username = self.room_name

        if user.is_authenticated and recipient_username:
            recipient = User.objects.filter(username=recipient_username).first()
            if recipient:
                Messages.objects.create(sender=user, recipient=recipient, messagetext=message)

        # Отправляем сообщение обратно в комнату с именем пользователя
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': User.username
            }
        )

    def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Отправляем сообщение обратно клиентам в комнате с именем пользователя
        self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

        
        