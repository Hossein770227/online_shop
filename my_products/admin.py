from .models import Prouduct
from django.contrib import admin


@admin.register(Prouduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','active','date_time_created',]