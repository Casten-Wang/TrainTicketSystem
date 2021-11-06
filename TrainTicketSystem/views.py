# -*- codeing = utf-8 -*-
# @Time:2021 11 04
# @Author: 王超凡
# @File:views.py
# @Software: PyCharm

from django.http import HttpResponse
from django.shortcuts import render


# 用户注册
def regist(request):
    ctx = {'site': u'百度', 'content': u'搜索引擎'}

    return render(request, "test1.html", ctx)
