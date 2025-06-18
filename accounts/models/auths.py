from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import ChoiceConstants
from django.contrib.auth import validators

class User(AbstractUser):
    password = models.CharField(
    )
    role = models.CharField(
        max_length=20,choices = ChoiceConstants.Role.choices, default = ChoiceConstants.Role.STUDENT
        )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'User'
    
    def __str__(self):
        return self.username