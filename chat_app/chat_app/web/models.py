from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Room(models.Model):
    NAME_MAX_LEN = 50
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        unique=True,
    )


class Message(models.Model):
    text = models.TextField()
    date = models.DateField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
