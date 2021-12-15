from django.db import models


# 车次表
class TrainTable(models.Model):
    train = models.CharField(max_length=20)
    maxpeople = models.IntegerField()
    begintime = models.DateTimeField()
    endtime = models.DateTimeField()
    origin = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    firstclassprice = models.FloatField()
    secondclassprice = models.FloatField()
