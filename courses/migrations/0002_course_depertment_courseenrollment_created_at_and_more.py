# Generated by Django 5.2.3 on 2025-06-18 13:29

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('depertments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='depertment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='depertments.depertment'),
        ),
        migrations.AddField(
            model_name='courseenrollment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseenrollment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='courseenrollment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='course',
            table='Course',
        ),
    ]
