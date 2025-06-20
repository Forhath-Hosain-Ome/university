# Generated by Django 5.2.3 on 2025-06-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('TEACHER', 'Teacher'), ('STUDENT', 'Student'), ('GUEST', 'Guest')], default='STUDENT', max_length=20),
        ),
    ]
