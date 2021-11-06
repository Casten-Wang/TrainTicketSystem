from django.contrib import admin
from TrainTicketSystem import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regist/', views.regist),
]
