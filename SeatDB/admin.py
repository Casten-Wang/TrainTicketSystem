from django.contrib import admin
from . import models

@admin.register(models.SeatTable)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['carriage', 'seat']
    list_editable = ['carriage', 'seat']
    list_per_page = 15
    list_display_links = None