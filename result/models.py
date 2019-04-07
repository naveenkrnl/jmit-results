from django.db import models

# Create your models here.

class ResultData(models.Model):
    studentid=models.IntegerField(null=True,blank=True)
    username=models.CharField(max_length=140, null=True, blank=True)
    email=models.CharField(max_length=140, null=True, blank=True)
    fullname=models.CharField(max_length=140, null=True, blank=True)
    phonenumber=models.CharField(max_length=140, null=True, blank=True)
    fathersname=models.CharField(max_length=140, null=True, blank=True)
    schoolname=models.CharField(max_length=140, null=True, blank=True)
    gender=models.CharField(max_length=140, null=True, blank=True)
    stream=models.CharField(max_length=140, null=True, blank=True)
    dob=models.DateField()
    rollno=models.CharField(max_length=140, null=True, blank=True)
    marks=models.IntegerField(blank=True)
    percentage=models.FloatField(blank=True)
    position=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.fullname