from django.contrib import admin
from django.urls import path, include, re_path
from UserDB import views

admin.site.site_header = '火车票管理系统'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.userlogin),
    path('user/', include('UserDB.urls')),
    path('index/', include('TrainDB.urls')),
]
