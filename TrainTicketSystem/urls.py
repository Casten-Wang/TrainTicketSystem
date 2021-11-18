from django.contrib import admin
from django.urls import path, include
from TrainTicketSystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('user/', include('UserDB.urls')),
    path('index/', include('TrainTicketDB.urls')),
]
