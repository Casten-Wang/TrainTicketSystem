from django.db import models
from SeatDB.models import SeatTable
from TrainDB.models import TrainTable
from UserDB.models import User


class TicketTable(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    trainId = models.ForeignKey(TrainTable, on_delete=models.CASCADE)
    seatId = models.ForeignKey(SeatTable, on_delete=models.CASCADE)
    # 购买时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    buytime = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.buytime

    class Meta:
        ordering = ['userId']
        verbose_name = '车票表'
        verbose_name_plural = '车票' # 表单名称