

from django.urls import path, include
from UserDB import views

urlpatterns = [
    path('regist/', views.userregist),
    path('login/', views.userlogin),
    path('addmoney/', views.addmoney)
]
