from django.db import models
from core.models import basemodel, ChoiceConstants
from depertments.models import Depertment
from accounts.models import User

class Event(basemodel):
    title = models.CharField(max_length=30, unique=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role' : ChoiceConstants.Role.TEACHER})
    depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE)
    