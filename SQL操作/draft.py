# -*- codeing = utf-8 -*-
# @Time:2021 11 15
# @Author: 王超凡
# @File:draft.py
# @Software: PyCharm

wf = open("数据csv/changedTrain.csv", mode="w")
count = 0
with open("数据csv/Train.csv", encoding="utf-16") as readfile:
    line = readfile.readline().strip()
    while line is not None and line != '':
        count += 1
        list1 = line.split(',')
        list1[-1] = str(int(int(list1[-2]) * 0.8))
        list1[2] = list1[2].split()[-1]
        list1[3] = list1[3].split()[-1]
        str1 = ",".join(list1)
        wf.write(str1 + '\n')
        line = readfile.readline().strip()

wf.close()
