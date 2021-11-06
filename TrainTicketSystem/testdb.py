# -*- codeing = utf-8 -*-
# @Time:2021 11 05
# @Author: 王超凡
# @File:testdb.py
# @Software: PyCharm

from django.http import HttpResponse

from TestModel.models import Test


# 数据库操作
def testdb(request):
    response = ""
    response1 = ""
    # 获取所有数据行，相当于 select * from
    list1 = Test.objects.all()
    # filter相当于SQL中的WHERE，可以设置条件过滤结果
    response2 = Test.objects.filter(id=1)
    # 获取单个对象
    response3 = Test.objects.get(id=1)
    # 限制返回的数据
    Test.objects.order_by('name')[0:2]
    # 数据排序
    Test.objects.order_by("id")

    Test.objects.filter(name="runoob").order_by("id")

    return HttpResponse("<p>" +  + "</p>")
