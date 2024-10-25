from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES= [
        ('DRIVER', 'Driver'),
        ('ADMIN', 'Admin'),
        ('CLIENT', 'Client'),
        ('DISPATCHER','Dispatcher'),
         ]
    
    role= models.CharField(max_length=10, choices= ROLE_CHOICES, default=ROLE_CHOICES[2]),
    birthdate= models.DateTimeField(editable=True, null=True, blank=True)
    address= models.CharField(max_length=200, blank=True)
    phone_number= models.CharField(max_length=15, blank=True)
    email= models.EmailField(unique=True)
    driver_license= models.CharField(max_length=20, blank=True, null=True)
        
    def is_admin(self):
        return self.role == self.ADMIN
            
    def is_client(self):
        return self.role == self.CLIENT
    def is_dispatcher(self):
        return self.role == self.DISPATCHER
    def is_driver(self):
        return self.role == self.DRIVER
            
    