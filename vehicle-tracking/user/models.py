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
        db_table = "users"
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
  

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Dispatcher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
