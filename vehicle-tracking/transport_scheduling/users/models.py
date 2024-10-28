# user/models.py
from django.contrib.auth.models import User,AbstractUser
from django.db import models
from django.conf import settings

class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('driver', 'Driver'),
        ('scheduler', 'Scheduler'),
        ('viewer', 'Viewer'),
        ('driver', 'Driver'),
        ('passenger', 'Passenger'),
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
class CustomUser(AbstractUser):
    pass
