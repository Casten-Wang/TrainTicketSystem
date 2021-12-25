from django.urls import path
from TicketDB import views

urlpatterns = [
    path('myticket/<my_id>', views.showTicket),
]
