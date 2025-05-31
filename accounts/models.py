from django.db import models
from courses.models import Course


class UserFields(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# Create your models here.
class Account(UserFields):
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        db_table = 'Account'
        ordering = ['username']
    
class Profile(UserFields):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    user_course = models.ManyToManyField(Course, blank=True, related_name='student')
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
        db_table = 'Profile'
        ordering = ['username']