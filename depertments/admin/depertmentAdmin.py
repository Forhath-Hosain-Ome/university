from django.contrib import admin
from depertments.models import depertment

@admin.register(depertment)
class DepertmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'major')
    search_fields = ('major', 'title')
    list_filter = ('major',)


