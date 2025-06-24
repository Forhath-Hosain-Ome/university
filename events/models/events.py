from django.db import models
from core.models import base_models, ChoiceConstants
from depertments.models import Depertment
from accounts.models import User

class Event(base_models):
    title = models.CharField(max_length=30, unique=True)
    host = models.ForeignKey(User, limit_choice_to={'role':ChoiceConstants.Role.TEACHER})
    depertment = models.ForeignKey(Depertment, on_delete=models.CASCADE)
    