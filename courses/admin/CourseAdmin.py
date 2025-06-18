from courses.models import Course
from django.contrib import admin

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date', 'price', 'instructor')
    ordering = ['instructor', 'depertment']
    search_fields = ['title', 'instructor']
    sortable_by = ['start_date', 'price', 'title', 'instructor']