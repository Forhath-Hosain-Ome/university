from django.db import models
from core.models import basemodel
from .user_account import User
from core.models import ChoiceConstants

class Profile(basemodel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    gender = models.CharField(
        max_length=10 ,choices=ChoiceConstants.Gender.choices, default=''
        )

    def __str__(self):
        return f"{self.user.username}'s Profile"
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
        db_table = 'Profile'