from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Employee(AbstractUser):
    ROLE = {
        ('Employee', 'Employee'),
        ('Admin', 'Admin'),
    }
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    password = models.CharField(max_length=140, default='Jalaj@12345')
    desg = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE)

    def __str__(self):
        return self.username