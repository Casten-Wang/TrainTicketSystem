# -*- codeing = utf-8 -*-
# @Time:2021 11 07
# @Author: 王超凡
# @File:urls.py
# @Software: PyCharm

from django.urls import path, include
from UserDB import views

urlpatterns = [
    path('regist/', views.userregist),
    path('login/', views.userlogin),
]
