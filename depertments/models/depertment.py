from django.db import models
from core.models import basemodel, ChoiceConstants



class Depertment(basemodel):
    title = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=99)
    major = models.CharField(max_length=10,choices=ChoiceConstants.Depertment,default='')
    images = models.ImageField(upload_to='media/images')

    def __str__(self):
        return self.title
    