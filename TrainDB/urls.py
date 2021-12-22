from django.urls import path
from TrainDB import views

urlpatterns = [
    path('main/', views.main),
    path('train/', views.showtrain),
]
