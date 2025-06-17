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

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'User'
    
    def __str__(self):
        return self.username