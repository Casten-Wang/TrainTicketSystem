from django.contrib import admin
from django.urls import path, include, re_path
from UserDB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.userlogin),
    path('user/', include('UserDB.urls')),
    path('index/', include('TrainDB.urls')),
]
