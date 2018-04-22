from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,default="none")
    password = models.CharField(max_length=100, default="none")
    key = models.CharField(max_length=100, default='00')

    def __str__(self):
        return self.name
