from django.contrib.auth.models import AbstractUser

from django.db import models

class User(AbstractUser):
    iban = models.CharField(max_length=22, default="DE11 1111 1111 1111 1111 11")


    def __str__(self) -> str:
        return self.username