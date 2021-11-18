# coding=utf-8
import os
import sys
import random
from datetime import date, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DC_PATH = "{0}\\SQL操作\\数据csv\\districtcode.txt".format(BASE_DIR)
print(DC_PATH)

codelist = []


class GetIDCard:
    # 随机生成身份证号
    @staticmethod
    def getdistrictcode():
        with open(DC_PATH) as file:
            data = file.read()
            districtlist = data.split('\n')
        for node in districtlist:
            # print node
            if node[10:11] != ' ':
                state = node[10:].strip()
            if node[10:11] == ' ' and node[12:13] != ' ':
                city = node[12:].strip()
            if node[10:11] == ' ' and node[12:13] == ' ':
                district = node[14:].strip()
                code = node[0:6]
                # 这里注意代码的缩进对齐位置
                codelist.append({"state": state, "city": city, "district": district, "code": code})

    @staticmethod
    def gennerator():
        if not codelist:
            GetIDCard.getdistrictcode()
        myid = codelist[random.randint(0, len(codelist))]['code']  # 地区项
        myid = myid + str(random.randint(1930, 2013))  # 年份项
        da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
        myid = myid + da.strftime('%m%d')
        myid = myid + str(random.randint(100, 300))  # ，顺序号简单处理

        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(0, len(myid)):
            count = count + int(myid[i]) * weight[i]
            myid = myid + checkcode[str(count % 11)]  # 算出校验码
            return myid
