from django.urls import path
from Backstage import views

urlpatterns = [
    path('train_delete', views.train_delete),
]
