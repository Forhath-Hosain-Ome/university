from django.contrib import admin
from events.models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
        list_display = ('title', 'host', 'depertment')
        sortable_by = ['title', 'host', 'depertment']
        search_fields = ['title', 'host', 'depertment']
        ordering = ['title', 'host', 'depertment']
