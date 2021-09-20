from django.db import models

class Insta(models.Model):
    user_name=models.CharField(max_length=100)
    user_mobile_number=models.BigIntegerField(unique=True)
    place=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,blank=True,null=True)
    profile_picture=models.ImageField(upload_to="images/%y/%m/%d",null=True)
    def _str_(self):
        return self.user_name

# Create your models here.
