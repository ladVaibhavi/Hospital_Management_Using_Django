from django.db import models
from ctypes import addressof
from email.headerregistry import Address
from django.db import models

       
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    bloodGroup = models.CharField(max_length=5)
    age = models.IntegerField()
    weight = models.IntegerField()
    Address = models.CharField(max_length=100)
    mobileNo = models.BigIntegerField()
    email= models.EmailField()
    password = models.CharField(max_length=100)

    def str(self):
        return super().title

class Hospital(models.Model):
    hospitalName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    ratings = models.FloatField()
    contactNo = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    def str(self):
        return self.title


class Doctor(models.Model):
    doctorName = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='images/')
    email = models.EmailField(max_length=100)
    specialist = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    mobileNo = models.BigIntegerField()
    morningTime = models.TimeField()
    eveningTime = models.TimeField()
    experience = models.FloatField()
    hospitalId = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    def str(self):
        return self.title

class Appointment(models.Model):
   patientId = models.ForeignKey(Patient,on_delete=models.CASCADE)
   doctorId = models.ForeignKey(Doctor,on_delete=models.CASCADE)
   time = models.TimeField()
   date = models.DateField()
   status = models.CharField(max_length=100)
   
   def str(self):
       return super().title