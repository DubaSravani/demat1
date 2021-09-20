from django.db import models
class Edubridge(models.Model):
     learners_name=models.CharField(max_length=100)
     address=models.TextField()
# Create your models here.
