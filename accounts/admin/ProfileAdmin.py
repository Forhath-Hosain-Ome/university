from django.contrib import admin
from accounts.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'date_of_birth', 'address', 'phone_number', 'gender')
    ordering = ['user']
    sortable_by = ['user', 'phone_number', 'gender']
    search_fields = ['user']