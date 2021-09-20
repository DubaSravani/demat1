from django.db import models
gen=[
('M','male'),
('F','female')
]

class Patient(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=10)
    gender=models.CharField(max_length=10,null=True,choices=gen)
    p_age=models.IntegerField(null=True)
    p_place=models.CharField(max_length=100)
    problem=models.TextField(null=True)
    def __str__(self):
        return self.p_name
class Hospital(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    h_name=models.CharField(max_length=100,default="sunrise hospital")
    location=models.CharField(max_length=100,default="Banglore")
    def __str__(self):
        return self.h_name

# Create your models here.
