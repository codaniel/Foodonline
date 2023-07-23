from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display =('email', 'fist_name', 'last_name','username', 'role','is_active','is_staff' )
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets =()

admin.register(User, CustomUserAdmin)