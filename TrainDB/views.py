from django.core.paginator import Paginator
from django.shortcuts import render

# 主页面
from TrainDB.models import TrainTable


def main(request):
    return render(request, 'main.html')


def showtrain(request):
    trainlst = TrainTable.objects.all()
    paginator = Paginator(trainlst, 10)
    current_num = request.GET.get('page')
    page = paginator.get_page(current_num)
    return render(request, 'train.html', {"page": page})
