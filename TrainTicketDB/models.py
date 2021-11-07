from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# 车次表
class TrainTable(models.Model):
    trainnum = models.CharField(max_length=10)
    maxpeople = models.IntegerField()
    begintime = models.TimeField()
    endtime = models.TimeField()
    origin = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    firstclassprice = models.FloatField()
    secondclassprice = models.FloatField()

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.trainnum
