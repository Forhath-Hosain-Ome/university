from courses.models import CourseEnrollment
from django.contrib import admin

@admin.register(CourseEnrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'enrollment_date')
    sortable_by = ['course', 'student', 'enrollment_date']
    search_fields = ['course', 'student']
    ordering = ['course', 'student']