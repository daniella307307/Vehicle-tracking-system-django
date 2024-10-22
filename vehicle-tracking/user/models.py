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
        
        
class Admin(User):
    class Meta:
        db_table ="admin-user"
    
    
class Driver(User):
    class Meta:
        db_table="driver"
        

class Dispatcher(User):
    class Meta:
        db_table = "dispatchers" 

class Customer(User):
    class Meta:
        db_table = "customers"