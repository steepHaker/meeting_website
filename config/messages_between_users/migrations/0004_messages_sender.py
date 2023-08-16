# Generated by Django 4.2.2 on 2023-08-02 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messages_between_users', '0003_rename_sender_messages_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='sender',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sender_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
