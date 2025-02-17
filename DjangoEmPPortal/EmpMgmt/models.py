from django.db import models

# Create your models here.
class Employee(models.Model):
    ROLE = {
        ('Employee', 'Employee'),
        ('Admin', 'Admin'),
    }
    Name = models.CharField(max_length=100)
    Desg = models.CharField(max_length=100)
    Role = models.CharField(max_length=20, choices=ROLE)

    def __str__(self):
        return self.Name