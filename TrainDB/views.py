from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

# 主页面
from TrainDB.models import TrainTable


def main(request):
    return render(request, 'index.html')


def showtrain(request):
    if request.method == "POST":
        print("提交购票信息")
        print(request.POST)
    print("车次查询")
    myorigin = request.GET["origin"]
    mydestination = request.GET["destination"]
    myDate = request.GET["begintime"]
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
