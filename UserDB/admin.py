from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','is_staff', 'sex', 'age', 'id_card', 'balance']

    list_editable = ['first_name', 'last_name', 'sex', 'age', 'id_card', 'balance']

    list_per_page = 15
    list_display_links = None