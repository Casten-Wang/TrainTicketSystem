from django.shortcuts import render, redirect
from UserDB.forms import UserRegisterForm, UserLoginForm
from UserDB.models import User
from django.contrib.auth import authenticate, login


# 用户注册
def userregist(request):
    if request.method == "POST":
        user_regist_form = UserRegisterForm(data=request.POST)
        print("!!!!!!!!!!!!")
        # 如果数据没有出错
        if user_regist_form.is_valid():
            print("OK")
            data = user_regist_form.cleaned_data
            print(data)
            User.objects.create_user(username=data["username"], password=data["password"], sex=data["sex"], age=data["age"], id_card=data["id_card"])
            return redirect('/user/login/')
        else:
            print(user_regist_form.errors)
    return render(request, 'regist.html')


# 用户登录
def userlogin(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])
            if user:
                login(request, user)
                return redirect('/index/main')
        else:
            print(user_login_form.errors)
    return render(request, 'login.html')


def addmoney(request):
    if request.method == "POST":
        print("POST")
        print(request.POST)
        myid = request.POST["myid"]
        money = request.POST["givemoney"]
        money = float(money)
        mybalance = float(User.objects.filter(id=myid).values_list('balance', flat=True)[0])
        User.objects.filter(id=myid).update(balance=mybalance + money)
        return redirect('/index/main')
    return render(request, 'bank.html')
