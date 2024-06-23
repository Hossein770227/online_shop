from django.contrib import admin

from .models import Product, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','date_time_created' ,'active']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'stars' , 'date_time_created', 'active']