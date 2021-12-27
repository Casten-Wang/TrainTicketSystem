from django.urls import path
from django.contrib import admin
from Backstage import views

urlpatterns = [
    path('myadmin', views.myadmin),
    path('train_add', views.train_add),
    path('train_change', views.train_change),
    path('maxpeople_change', views.maxpeople_change),
    path('begintime_change', views.begintime_change),
    path('endtime_change', views.endtime_change),
    path('origin_change', views.origin_change),
    path('destination_change', views.destination_change),
    path('firstclassprice_change', views.firstclassprice_change),
    path('secondclassprice_change', views.secondclassprice_change),
    path('user_delete', views.user_delete),
    path('username_change', views.username_change),
    path('sex_change', views.sex_change),
    path('age_change', views.age_change),
    path('IDcard_change', views.IDcard_change),
    path('balance_change', views.balance_change),
    path('ticket_delete', views.ticket_delete),
    path('ticket_add', views.ticket_add),
    path('admin/', admin.site.urls),
    path('ticket_userid_change', views.ticket_userid_change),
    path('ticket_trainid_change', views.ticket_trainid_change),
    path('ticket_seatid_change', views.ticket_seatid_change),
    path('ticket_price_change', views.ticket_price_change),
    path('seat_delete', views.seat_delete),
    path('seat_add', views.seat_add),
    path('seat_seatid_change', views.seat_seatid_change),
    path('seat_carriage_change', views.seat_carriage_change),
    path('seat_seat_change', views.seat_seat_change),

]
