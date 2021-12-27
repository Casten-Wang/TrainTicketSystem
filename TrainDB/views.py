from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

# 主页面
from TrainDB.models import TrainTable
from UserDB.models import User
from TicketDB.models import TicketTable
from SeatDB.models import SeatTable


def main(request):
    return render(request, 'index.html')

def showtrain(request):
    if request.method == "POST":
        print("提交购票信息")
        print(request.POST)
        mybalance = float(User.objects.filter(username=request.POST["myname"]).values_list('balance', flat=True)[0])
        print("余额：", mybalance)
        ticketClass = request.POST["Seat"]
        ticketClass = "firstclassprice" if ticketClass == "一等座" else "secondclassprice"
        print("座位类型：", ticketClass)
        trainTicket = float(TrainTable.objects.filter(id=request.POST["trainID"]).values_list(ticketClass, flat=True)[0])
        print("票价", trainTicket)
        print("检查该用户是否已经购买该车次")
        notBuyFlag = True
        userID = User.objects.filter(username=request.POST["myname"]).values_list('id', flat=True)[0]
        trainID = request.POST["trainID"]
        isBuyThisTrain = TicketTable.objects.filter(userId_id=userID, trainId_id=trainID)
        print(isBuyThisTrain)
        if len(isBuyThisTrain) == 0:
            print("尚未购买该车次，可以购买!")
            if notBuyFlag and (mybalance - trainTicket) >= 0:
                print("余额充足")
                print("查看余票是否充足")
                userID = User.objects.filter(username=request.POST["myname"]).values_list('id', flat=True)[0]
                trainID = request.POST["trainID"]
                print("----------")
                firstSeatSoldList = TicketTable.objects.filter(trainId_id=trainID, seatId_id__gte=1, seatId_id__lte=5).values_list("seatId_id", flat=True)
                secondSeatSoldList = TicketTable.objects.filter(trainId_id=trainID, seatId_id__gte=6, seatId_id__lte=20).values_list("seatId_id", flat=True)
                print("一等座已售座位表：", firstSeatSoldList)
                print("二等座已售座位表：", secondSeatSoldList)
                firstSeatSoldNum = len(firstSeatSoldList)
                print("一等座已售票数：", firstSeatSoldNum)
                secondSeatSoldNum = len(secondSeatSoldList)
                print("二等座已售票数：", secondSeatSoldNum)
                print("----------")
                firstSeatNotSoldNum = 5 - firstSeatSoldNum
                secondSeatNotSoldNum = 15 - secondSeatSoldNum
                print("----------")
                if ticketClass == "firstclassprice" and firstSeatNotSoldNum > 0:
                    print("用户购买一等票，开始安排一等票座位")
                    firstAllList = range(1, 6)
                    print(firstAllList)
                    firstChoiceList = [i for i in firstAllList if i not in firstSeatSoldList]
                    print(firstChoiceList)
                    print("开始生成订单")
                    TicketTable.objects.create(seatId_id=firstChoiceList[0], trainId_id=trainID, userId_id=userID, price=trainTicket)
                    print("开始修改余额")
                    User.objects.filter(username=request.POST["myname"]).update(balance=(mybalance - trainTicket))
                    result = "订票成功"
                elif ticketClass == "secondclassprice" and secondSeatNotSoldNum > 0:
                    print("用户购买二等票，开始安排二等票座位")
                    secondAllList = range(6, 21)
                    print(secondAllList)
                    secondChoiceList = [i for i in secondAllList if i not in secondSeatSoldList]
                    print(secondChoiceList)
                    print("开始生成订单")
                    TicketTable.objects.create(seatId_id=secondChoiceList[0], trainId_id=trainID, userId_id=userID, price=trainTicket)
                    print("开始修改余额")
                    User.objects.filter(username=request.POST["myname"]).update(balance=(mybalance - trainTicket))
                    result = "订票成功"
                else:
                    print("余票不足")
                    result = "余票不足"
            else:
                print("余额不足")
                result = "余额不足"
        else:
            print("已经购买该车次，不能重复购票!")
            result = "已经购买该车次，不能重复购票"

    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("车次查询")
    myorigin = request.GET["origin"]
    mydestination = request.GET["destination"]
    myDate = request.GET["begintime"]

    # 发现出发地或者目标地或者日期尚未输入
    if myorigin == "" or mydestination == "" or myDate == "":
        return render(request, 'index.html')

    print(myDate)
    myyear, mymonth, myday = myDate.split('-')
    datetime_filter = datetime(int(myyear), int(mymonth), int(myday))
    trainlst = TrainTable.objects.filter(Q(origin=request.GET["origin"]) & Q(destination=request.GET["destination"]) & Q(begintime__startswith=datetime_filter.date()))
    print(trainlst)
    print(len(trainlst))
    paginator = Paginator(trainlst, 10)
    current_num = request.GET.get('page')
    page = paginator.get_page(current_num)
    return render(request, 'train.html', locals())
