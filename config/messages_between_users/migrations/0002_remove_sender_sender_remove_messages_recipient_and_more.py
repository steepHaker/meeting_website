# Generated by Django 4.2.2 on 2023-07-31 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messages_between_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sender',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='recipient',
        ),
        migrations.AlterField(
            model_name='messages',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Recipient',
        ),
        migrations.DeleteModel(
            name='Sender',
        ),
    ]
