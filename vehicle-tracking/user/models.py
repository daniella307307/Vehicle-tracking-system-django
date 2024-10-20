from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    Role = (
        ('admin', 'Admin'),
        ('driver', 'Driver'),
        ('dispatcher', 'Dispatcher'),
        ('customer', 'Customer'),
        )
    role = models.CharField(max_length=15, choices=Role)
    def __str__(self) -> str:
        return super().__str__()

class Meta:
    db_name= "users"