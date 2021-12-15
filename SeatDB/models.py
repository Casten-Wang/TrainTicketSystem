from django.db import models


# 座位表
class SeatTable(models.Model):
    carriage = models.CharField(max_length=10)
    seat = models.CharField(max_length=10)
