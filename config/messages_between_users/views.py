from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from messages_between_users.serializers import MassagesSerializer
from .models import Messages
from .forms import MessageForm
from .models import User
from django.db.models import Q

class SendMessageView(APIView):
    def get(self, request, username, *args, **kwargs):
        user = request.user
        other_user = get_object_or_404(User, username=username)
        messages = Messages.objects.filter(Q(recipient=user, sender=other_user) | Q(recipient=other_user, sender=user)).order_by('date', 'time')
        form = MessageForm()
        context = {'form': form, 'username': username, 'messages': messages}
        return render(request, 'user_message/messages-list.html', context)

    
    def post(self, request, username):
            messagetext = request.data.get('messagetext')

            try:
                recipient = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'Error': "Recipient not found"}, status=status.HTTP_400_BAD_REQUEST)

            message = Messages.objects.create(sender=request.user, recipient=recipient, messagetext=messagetext)
            serializer = MassagesSerializer(message)

            # Return the response as JsonResponse with the serialized data
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    


@login_required
def chat_with_user(request):
    # Получаем список пользователей, с которыми у нас есть переписка
    user = request.user
    users_with_messages = message.objects.filter(
        Q(sender=user) | Q(recipient=user)
    ).distinct('sender', 'recipient')
    
    # Вы можете добавить дополнительные поля в users_with_messages, например, чтобы отображать последнее сообщение
    # users_with_messages = users_with_messages.annotate(last_message=Max('timestamp'))

    return render(request, 'messages.html', {'users': users_with_messages})
