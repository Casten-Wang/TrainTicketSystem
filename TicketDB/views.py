from django.shortcuts import render

# Create your views here.

from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

from TicketDB.models import TicketTable
from UserDB.models import User


def showTicket(request, my_id):
    if request.method == "POST":
        print("退票")
        print(request.POST)
        ticketID = request.POST["ticketID"]
        print("返还钱")
        mybalance = float(User.objects.filter(id=my_id).values_list('balance', flat=True)[0])
        print("余额", mybalance)
        ticketPrice = float(TicketTable.objects.filter(id=ticketID).values_list('price', flat=True)[0])
        print("票价", ticketPrice)
        User.objects.filter(id=my_id).update(balance=(mybalance + ticketPrice))
        print("删除车票")
        TicketTable.objects.get(id=ticketID).delete()
        result = "车票删除成功"
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("本人车票查询")
    page = TicketTable.objects.filter(userId_id=my_id)
    print(page)
    print(len(page))
    return render(request, 'myticket.html', locals())
