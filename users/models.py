from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    telegram_chat_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='Telegram chat ID')

    def __str__(self):
        return self.email
