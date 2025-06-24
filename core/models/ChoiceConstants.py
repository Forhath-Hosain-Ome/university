from django.db import models

class ChoiceConstants:
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        TEACHER = 'TEACHER', 'Teacher'
        STUDENT = 'STUDENT', 'Student'
        GUEST = 'GUEST', 'Guest'

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    class Depertment(models.TextChoices):
        CSE = 'CSE', 'Computer Science and Engineering'
        EEE = 'EEE', 'Electrical and Electronics Engineering'
        CIVIL = 'CIVIL', 'Civil Engineering'
        MECHANICAL = 'MECHANICAL', 'Mechanical Engineering'
        CHEMICAL = 'CHEMICAL', 'Chemical Engineering'