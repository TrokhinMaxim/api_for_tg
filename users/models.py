from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    active_follow = models.BooleanField(default=False)


class CurrencyRequest(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    exchange_rate = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"


from django.db import models


class Text(models.Model):
    name = models.CharField(max_length=255, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.name
