from django.contrib import admin
from . import models


@admin.register(models.TrainTable)
class TrainAdmin(admin.ModelAdmin):
    list_display = ['train', 'maxpeople', 'begintime', 'endtime',
                    'origin', 'destination', 'firstclassprice',
                    'secondclassprice']
    list_editable = [ 'maxpeople', 'begintime', 'endtime',
                    'origin', 'destination', 'firstclassprice',
                    'secondclassprice']
    list_per_page = 15

