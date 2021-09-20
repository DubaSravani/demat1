from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
def validate_delhi(value):
    if "delhi" in value:
        return value
    elif "india_delhi" in value:
        return value
    else:
         raise ValidationError("delhi place")
def validate_com(value):
    if "Excellent" or "very good" or "good" in value:
        return value
    else:
        raise ValidationError("pls give good comments")

class Post(models.Model):
    name =models.CharField(max_length=100)
    address=models.CharField(max_length=100)

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=200)
    author_name=models.CharField(max_length=200)
    comments=models.CharField(max_length=200,blank=True,null=True,validators=[validate_com])
    place=models.CharField(max_length=200,default='Andhra')
    review=models.CharField(max_length=200,blank=True,null=True)
    present=models.BooleanField(null=True)
    num=models.BigIntegerField(null=True)
    student_date=models.DateTimeField(default=timezone.now())
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    student_updated=models.DateTimeField(auto_now=True,null=True)
    rating=models.TextField(blank=True,null=True,help_text="pls fill rating staring from 5")
    email=models.EmailField(default="sravs@gamil.com")
    profile_pic=models.ImageField(upload_to="images/%y/%m/%d",null=True)
    resume=models.FileField(upload_to="userfiles/%y/%m/%d",null=True)
    address=models.CharField(max_length=250,validators=[validate_delhi])
    rating=models.TextField(null=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.rating:
            self.rating="fivestar"
        super(student,self).save(*args,**kwargs)

    def __str__(self):
        return self.book_name
