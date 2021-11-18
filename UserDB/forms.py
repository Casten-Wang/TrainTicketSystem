# -*- codeing = utf-8 -*-
# @Time:2021 11 07
# @Author: 王超凡
# @File:forms.py.py
# @Software: PyCharm

from django import forms
from UserDB.models import User


class UserRegisterForm(forms.ModelForm):
    class Meta:
        # 要关联的模型
        model = User
        # 设置表单中使用的字段
        fields = ['username', 'password', 'sex', 'age', 'id_card']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
