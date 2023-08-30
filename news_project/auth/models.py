from django.db import models
from django.contrib.auth.models import User
from oauth2_provider.models import AbstractApplication


class OAuth2Client(AbstractApplication):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

