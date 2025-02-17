from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Desg = models.CharField(max_length=100)
    # Email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return self.Name