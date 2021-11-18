from django.core.paginator import Paginator
from django.shortcuts import render

# 主页面
from TrainTicketDB.models import TrainTable


def main(request):
    trainlst = TrainTable.objects.all()
    print(trainlst)
    paginator = Paginator(trainlst, 3)
    page = request.GET.get('page')
    train = paginator.get_page(page)
    print(train.object_list)

    return render(request, 'draft.html')
