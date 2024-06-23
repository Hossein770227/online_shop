from django.contrib import admin

from .models import Product, Comment


class CommentTabularInline(admin.TabularInline):
    model = Comment
    fields =  ['author','text', 'stars' , 'active']
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','date_time_created' ,'active']
    inlines = [CommentTabularInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'stars' , 'date_time_created', 'active']