from django.db import models
from core.models import basemodel
from accounts.models import User

class Course(basemodel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    instructor = models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to={'Roles':'teacher'})


    def __str__(self):
        return self.title