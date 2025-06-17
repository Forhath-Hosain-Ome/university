from django.contrib import admin
from accounts.models import User

@admin.register(User)
class AuthAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    ordering = ['username']
    sortable_by = ['username', 'email', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'is_staff', 'is_active']