from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password


class User(AbstractUser):
    sex = models.CharField(max_length=5)
    age = models.IntegerField()
    id_card = models.CharField(max_length=20)
    balance = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        ordering = ['first_name']
        verbose_name = '用户信息'
        verbose_name_plural = '用户' # 表单名称
