# Generated by Django 5.1.2 on 2024-11-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('driver', 'Driver'), ('scheduler', 'Scheduler'), ('viewer', 'Viewer'), ('driver', 'Driver'), ('passenger', 'Passenger')], default='Viewer', max_length=20),
        ),
    ]
