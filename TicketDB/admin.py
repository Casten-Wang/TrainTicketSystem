from django.contrib import admin
from . import models


@admin.register(models.TicketTable)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['userId', 'trainId', 'seatId', 'buytime']
    list_editable = ['userId', 'trainId', 'seatId']
    list_per_page = 15
    list_display_links = None
