from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin




from .forms import UserCreationForm, UserChangeForm
from .models import MyUser



class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["full_name","phone_number", "is_active",  "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["full_name","phone_number" ,"password"]}),
        ("Permissions", {"fields": ["is_admin","is_active", "last_login"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["full_name", "phone_number", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["full_name"]
    ordering = ["full_name"]
    filter_horizontal = []



admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)
