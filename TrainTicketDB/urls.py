# -*- codeing = utf-8 -*-
# @Time:2021 11 07
# @Author: 王超凡
# @File:urls.py
# @Software: PyCharm


from django.urls import path
from TrainTicketDB import views

urlpatterns = [
    path('main/', views.main),
]
