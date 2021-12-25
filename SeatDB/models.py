from django.db import models


# 座位表
class SeatTable(models.Model):
    carriage = models.CharField(max_length=10)
    seat = models.CharField(max_length=10)

    class Meta:
        ordering = ['seat']
        verbose_name = '座位表'
        verbose_name_plural = '座位'  # 表单名称
