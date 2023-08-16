from django.db import models
from ckeditor.fields import RichTextField

from meeting_create_user.models import User


class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender_user")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    messagetext = RichTextField(max_length=5000)
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    