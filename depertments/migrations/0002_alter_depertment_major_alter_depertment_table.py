# Generated by Django 5.2.3 on 2025-06-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depertments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depertment',
            name='major',
            field=models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('CIVIL', 'Civil Engineering'), ('MECHANICAL', 'Mechanical Engineering'), ('CHEMICAL', 'Chemical Engineering')], default='', max_length=10),
        ),
        migrations.AlterModelTable(
            name='depertment',
            table='Depertment',
        ),
    ]
