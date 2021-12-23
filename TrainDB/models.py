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

    def __str__(self) -> str:
        return self.train

    class Meta:
        ordering = ['train']
        verbose_name = '火车'
        verbose_name_plural = '车次' # 表单名称
