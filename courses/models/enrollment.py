from django.db import models
from .course import Course
from accounts.models import User

class CourseEnrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, limit_choices_to={'Roles':'student'}, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"