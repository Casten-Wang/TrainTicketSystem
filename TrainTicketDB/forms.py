# -*- codeing = utf-8 -*-
# @Time:2021 11 07
# @Author: 王超凡
# @File:forms.py.py
# @Software: PyCharm

from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=20)
    password = forms.CharField(label="密码", max_length=30, widget=forms.PasswordInput)
    sex = forms.ChoiceField(choices=((1, "男"), (2, "女")))
    age = forms.IntegerField(label="年龄")
    id_card = forms.CharField(label="身份证号", max_length=20)

