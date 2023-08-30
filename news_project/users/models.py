from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    confirmation_token = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.email


User.groups.field.remote_field.related_name = 'user_related_groups'
User.user_permissions.field.remote_field.related_name = 'user_related_permissions'
