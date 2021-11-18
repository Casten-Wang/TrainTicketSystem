from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password


class User(AbstractUser):
    sex = models.CharField(max_length=5)
    age = models.IntegerField()
    id_card = models.CharField(max_length=20)
