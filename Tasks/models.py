from django.db import models
from django import forms

# Create your models here.
class Task(models.Model):
    Status_CHOICES = [
          ('Open', 'Opened'),
        ('Completed', 'Completed'),
        ('Postponed', 'Postponed'),
        ('Reassigned', 'Reassigned'),
        ('Canceled', 'Canceled'),
        ('Rescheduled', 'Rescheduled')
         ]
    title=models.CharField( max_length=50)   
    description=models.CharField( max_length=50)
    assigned_to=models.ForeignKey('Employee', on_delete=models.CASCADE )
    
    status = models.CharField( max_length=20,choices=Status_CHOICES,null=True,default='Open')
    department=models.ForeignKey("Department", on_delete=models.CASCADE)
    progress=models.FloatField()
    
def __str__(self) -> str:
        return self.title

class Department(models.Model):
    
     title=models.CharField( max_length=50)
     
def __str__(self) -> str:
        return self.title

class Employee(models.Model):
   
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)

def __str__(self) -> str:
        return self.first_name

