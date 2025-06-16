from django.db import models
from django.contrib.auth.models import AbstractUser

Roles = (
    ('admin', 'Admin'),
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('guest', 'Guest'),
)

class User(AbstractUser):
    role = models.Choices(Roles, default = 'guest')

    def __str__(self):
        return self.username