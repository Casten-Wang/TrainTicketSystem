# -*- codeing = utf-8 -*-
# @Time:2021 11 04
# @Author: 王超凡
# @File:views.py
# @Software: PyCharm

from django.http import HttpResponse
from django.shortcuts import render
from TrainTicketDB.forms import UserRegisterForm
from django.contrib import auth
from django.contrib.auth.models import User


# 用户注册
def regist(request):
    if request.method == "POST":
        user_regist_form = UserRegisterForm(data=request.POST)
        print("!!!!!!!!!!!!")
        # 如果数据没有出错
        if user_regist_form.is_valid():
            # 清洗出合法数据
            data = user_regist_form.cleaned_data
            User.objects.create_user(username=)
        else:
            print(user_regist_form.errors)
    return render(request, 'regist.html')


# 用户登录
def login(request):
    return render(request, 'login.html')
