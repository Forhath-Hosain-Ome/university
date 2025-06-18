from django.db import models
from core.models import basemodel

Depertment_choice = (
    ("CSE",'CSE'),
    ('EEE','EEE'),
    ('CIVIL','CIVIL'),
)

class depertment(basemodel):
    title = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=99)
    major = models.CharField(max_length=10,choices=Depertment_choice,default='')
    images = models.ImageField(upload_to='media/images')