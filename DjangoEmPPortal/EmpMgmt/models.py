from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Desg = models.CharField(max_length=100)