from django.contrib import admin
from django.urls import path, include, re_path
from UserDB import views


urlpatterns = [
    path('', include('Backstage.urls')),
    path('user/', include('UserDB.urls')),
    path('index/', include('TrainDB.urls')),
    path('ticket/', include('TicketDB.urls')),
]
