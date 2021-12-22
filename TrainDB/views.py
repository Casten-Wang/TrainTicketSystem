from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

# 主页面
from TrainDB.models import TrainTable


def main(request):
    return render(request, 'index.html')


def showtrain(request):
    if request.method == "GET":
        print("车次查询")
        print()
        myDate = request.GET["begintime"]
        print(myDate)
        myyear, mymonth, myday = myDate.split('-')
        print(myyear)
        print(mymonth)
        print(myday)
        trainlst = TrainTable.objects.filter(Q(origin=request.GET["origin"]) & Q(destination=request.GET["destination"]) & Q(begintime__year=myyear, begintime__month=mymonth, begintime__day=myday))
        print(trainlst)
        print(len(trainlst))
        paginator = Paginator(trainlst, 10)
        current_num = request.GET.get('page')
        page = paginator.get_page(current_num)
        return render(request, 'train.html', {"page": page})
