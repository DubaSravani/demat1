from django.db import models
class Intro(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    mob=models.CharField(max_length=10,blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    date_of_birth=models.DateField(blank=True,null=True)
    
# Create your models here.
