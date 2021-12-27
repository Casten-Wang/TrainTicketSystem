# Create your views here.

from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q

from SeatDB.models import SeatTable
from TicketDB.models import TicketTable
from UserDB.models import User

from django.shortcuts import render, redirect

from TrainDB.models import TrainTable


def train_delete(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        myid = request.POST["id"]
        print("delete")
        data = TrainTable.objects.get(id=id)
        data.delete()
        return redirect('/admin/#/admin/TrainDB/traintable/')


def train_add(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        myid = request.POST.get["id"]
        train = request.POST.get('train')
        maxpeople = request.POST.get('maxpeople')
        begintime = request.POST.get('begintime')
        endtime = request.POST.get('endtime')
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        firstclassprice = request.POST.get('firstclassprice')
        secondclassprice = request.POST.get('secondclassprice')
        data = TrainTable()
        data.train = train
        data.maxpeople = maxpeople
        data.begintime = begintime
        data.endtime = endtime
        data.origin = origin
        data.destination = destination
        data.firstclassprice = firstclassprice
        data.secondclassprice = secondclassprice
        data.save()
        print("add")
        return redirect('/admin/#/admin/TrainDB/traintable/')


def train_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_train = request.POST["train"]
        print("修改")
        data = TrainTable.objects.update(train=my_train)
        return redirect('/admin/#/admin/TrainDB/traintable/')


def maxpeople_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_maxpeople = request.POST["maxpeople"]
        print("修改")
        data = TrainTable.objects.update(maxpeople=my_maxpeople)
        return redirect('/admin/#/admin/TrainDB/traintable/')


def begintime_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_begintime = request.POST["begintime"]
        print("修改")
        data = TrainTable.objects.update(begintime=my_begintime)
        return redirect('/admin/#/admin/TrainDB/traintable/')


def endtime_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_endtime = request.POST["begintime"]
        print("修改")
        data = TrainTable.objects.update(endtime=my_endtime)
        return redirect('/admin/#/admin/TrainDB/traintable/')


def origin_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_origin = request.POST["origin"]
        print("修改")
        data = TrainTable.objects.update(origin=my_origin)
        return redirect('/admin/#/admin/TrainDB/traintable/')


def destination_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_destination = request.POST["destination"]
        print("修改")
        data = TrainTable.objects.update(destination=my_destination)
        return redirect('/admin/#/admin/TrainDB/traintable/')


def firstclassprice_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_firstclassprice = request.POST["firstclassprice"]
        print("修改")
        data = TrainTable.objects.update(firstclassprice=my_firstclassprice)
        return redirect('/admin/#/admin/TrainDB/traintable/')


def secondclassprice_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_secondclassprice = request.POST["secondclassprice"]
        print("修改")
        data = TrainTable.objects.update(secondclassprice=my_secondclassprice)
        return redirect('/admin/#/admin/TrainDB/traintable/')


def user_delete(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        myid = request.POST["id"]
        print("delete")
        data = User.objects.get(id=id)
        data.delete()
        return redirect('/admin/#/admin/UserDB/user/')


def user_add(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        myid = request.POST.get["id"]
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        IDcard = request.POST.get('IDcard')
        balance = request.POST.get('balance')
        data = User()
        data.id = myid
        data.name = name
        data.sex = sex
        data.age = age
        data.IDcard = IDcard
        data.balance = balance
        data.save()
        print("add")
        return redirect('/admin/#/admin/UserDB/user/')


def username_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_name = request.POST["name"]
        print("修改")
        data = User.objects.update(username=my_name)
        return redirect('/admin/#/admin/UserDB/user/')


def sex_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_sex = request.POST["sex"]
        print("修改")
        data = User.objects.update(sex=my_sex)
        return redirect('/admin/#/admin/UserDB/user/')


def age_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_age = request.POST["age"]
        print("修改")
        data = User.objects.update(age=my_age)
        return redirect('/admin/#/admin/UserDB/user/')


def IDcard_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_IDcard = request.POST["IDcard"]
        print("修改")
        data = User.objects.update(id_card=my_IDcard)
        return redirect('/admin/#/admin/UserDB/user/')


def balance_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_balance = request.POST["balance"]
        print("修改")
        data = User.objects.update(balance=my_balance)
        return redirect('/admin/#/admin/UserDB/user/')


def ticket_delete(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        myid = request.POST["id"]
        print("delete")
        data = TicketTable.objects.get(id=myid)
        data.delete()
        return redirect('/admin/#/admin/TicketDB/tickettable/')


def ticket_add(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        myid = request.POST.get["id"]
        userid = request.POST.get('userid')
        trainid = request.POST.get('trainid')
        seatid = request.POST.get('seatid')
        data = TicketTable()
        data.id = myid
        data.userid = userid
        data.trainid = trainid
        data.seatid = seatid
        data.save()
        print("add")
        return redirect('/admin/#/admin/TicketDB/tickettable/')


def ticket_userid_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_name = request.POST["name"]
        print("修改")
        data = TrainTable.objects.update(userId_id=my_name)
        return redirect('/admin/#/admin/TicketDB/tickettable/')


def ticket_trainid_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_trainid = request.POST["trainid"]
        print("修改")
        data = User.objects.update(trainId_id=my_trainid)
        return redirect('/admin/#/admin/TicketDB/tickettable/')


def ticket_seatid_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_trainid = request.POST["seatnid"]
        print("修改")
        data = User.objects.update(seatId_id=my_trainid)
        return redirect('/admin/#/admin/TicketDB/tickettable/')


def ticket_price_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_price = request.POST["price"]
        print("修改")
        data = User.objects.update(price=my_price)
        return redirect('/admin/#/admin/TicketDB/tickettable/')


def seat_delete(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        myid = request.POST["id"]
        print("delete")
        data = SeatTable.objects.get(id=myid)
        data.delete()
        return redirect('/admin/#/admin/SeatDB/seattable/')


def seat_add(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        seatid = request.POST.get('seatid')
        carriage = request.POST.get('carriage')
        seat = request.POST.get('seat')
        data = SeatTable()
        data.id = seatid
        data.carriage = carriage
        data.seat = seat
        data.save()
        print("add")
        return redirect('/admin/#/admin/SeatDB/seattable/')


def seat_seatid_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_seatid = request.POST["seatid"]
        print("修改")
        data = SeatTable.objects.update(id=my_seatid)
        return redirect('/admin/#/admin/SeatDB/seattable/')


def seat_carriage_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_carriage = request.POST["carriage"]
        print("修改")
        data = SeatTable.objects.update(carriage=my_carriage)
        return redirect('/admin/#/admin/SeatDB/seattable/')


def seat_seat_change(request):
    if request.method == "POST":
        print("GET the POST")
        print(request.POST)
        my_seat = request.POST["seat"]
        print("修改")
        data = SeatTable.objects.update(seat=my_seat)
        return redirect('/admin/#/admin/SeatDB/seattable/')
