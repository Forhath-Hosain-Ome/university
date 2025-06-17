from django.db import models
from django.contrib.auth.models import AbstractUser

Roles = (
    ('admin', 'Admin'),
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('guest', 'Guest'),
)

class User(AbstractUser):
    password = models.CharField()
    role = models.CharField(max_length=20,choices = Roles, default = 'guest')

    def __str__(self):
        return self.username