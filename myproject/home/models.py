from django.db import models

# Create your models here.
class Contact(models.Model):
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    
    
    
    