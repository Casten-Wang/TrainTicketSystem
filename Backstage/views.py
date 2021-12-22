from django.shortcuts import render

# Create your views here.
#删除车次信息
from TrainDB.models import TrainTable


def train_delete(request,id):
    ob = TrainTable.objects.get(id=id)
    ob.delete()
    return render(request, "404.html")

#修改车次信息
def train_rectify(request,id):
    ob = TrainTable.objects.get(id=request.POST['id'])
    ob.maxpeople = request.POST['maxpeople']
    ob.begintime = request.POST['begintime']
    ob.endtime = request.POST['endtime']
    ob.origin = request.POST['origin']
    ob.destination = request.POST['destination']
    ob.firstclassprice = request.POST['firstclassprice']
    ob.secondclassprice = request.POST['secondclassprice']
    ob.save()
    return render(request, "404.html")

#增加车次信息
def train_add(request):
    ob = TrainTable()
    ob.train = request.POST.get('train')
    ob.maxpeople = request.POST.get('maxpeople')
    ob.begintime = request.POST.get('begintime')
    ob.endtime = request.POST.get('endtime')
    ob.origin = request.POST.get('origin')
    ob.destination = request.POST.get('destination')
    ob.firstclassprice = request.POST.get('firstclassprice')
    ob.secondclassprice = request.POST.get('secondclassprice')
    ob.save()
    return render(request, "404.html")
