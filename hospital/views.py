from asyncio.windows_events import NULL
from ctypes import addressof
import imp
from pydoc import doc
from pyexpat import model
from time import time
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from pkg_resources import to_filename
from .models import Appointment, Patient,Doctor,Hospital
from PIL import Image
import datetime 
from datetime import datetime

def registration(request):
    if(request.method=='POST'):
        type=request.POST.get("category")
        print(type)
        if(type=="Patient"):
            return redirect('addPatient')
        elif(type=="Hospital"):
            return redirect('addHospital')
    else:
        return render(request,'registration.html')
    return render(request,'temp.html')

def addPatient(request):
    if(request.method == 'POST'):
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if(password == cpassword):
            if(Patient.objects.filter(name=request.POST['name']).exists() or Patient.objects.filter(email=request.POST['email']).exists()):
                return redirect('register')
            patient=Patient()
            patient.name = request.POST['name']
            patient.dob = request.POST['dob']
            patient.bloodGroup = request.POST['bg']
            patient.age = request.POST['age']
            patient.weight = request.POST['weight']
            patient.Address = request.POST['address']
            patient.mobileNo = request.POST['mobile']
            patient.email= request.POST['email']
            patient.password = request.POST['password']
            patient.save()
            return render(request,'temp.html')
    return render(request,'patient.html')
    
def addHospital(request):
    if(request.method == 'POST'):
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if(password == cpassword):
            if(Hospital.objects.filter(hospitalName = request.POST['hname']).exists()):
                return render(request,'hospital.html')
            hospital = Hospital()
            hospital.hospitalName = request.POST['hname']
            hospital.address = request.POST['address']
            hospital.contactNo = request.POST['contactNo']
            hospital.email = request.POST['email']
            hospital.ratings = 3
            hospital.password = request.POST['password']
            hospital.save()
            return render(request,'login.html')
    return render(request,'hospital.html')

def loginHospital(request):
    if (request.method == 'POST'):
        if(Hospital.objects.filter(hospitalName = request.POST['name']).exists() and Hospital.objects.filter(password = request.POST['password']).exists()):
            request.session['hid'] = Hospital.objects.get(hospitalName = request.POST['name']).id
    return render(request,'login.html')

def loginPatient(request):
    if(request.method=='POST'):
        if(Patient.objects.filter(name = request.POST['name']).exists() and Patient.objects.filter(password = request.POST['password']).exists()):
            request.session['pid']= Patient.objects.get(name = request.POST['name']).id
            return render(request,'temp.html')
    return render(request,'login.html')

def addDoctor(request):
    if (request.method == 'POST'):
        if( Doctor.objects.filter(doctorName=request.POST['dname']).exists() or Doctor.objects.filter(email=request.POST['email']).exists()):
            return redirect('register')
        doctor = Doctor()
        doctor.image = request.FILES['image']
        doctor.doctorName = request.POST['dname']
        doctor.email = request.POST['email']
        doctor.specialist = request.POST['specialition']
        doctor.gender = request.POST['gender']
        doctor.mobileNo = request.POST['mobile']
        doctor.morningTime = request.POST['morningTime']
        doctor.eveningTime = request.POST['eveningTime']
        doctor.experience = request.POST['exeperience']
        doctor.password = request.POST['password']
        doctor.hospitalId = Hospital.objects.get(id=1)
        doctor.save()
        return render(request,'temp.html')
    return render(request,'doctor.html')

def addAppointment(request,did):
    if(request.method=='POST'):
        if(request.session['pid'] != NULL and Doctor.objects.filter(id=did).exists()):
            appointments = list(Appointment.objects.filter(doctorId=did))
            if(len(appointments) == 0):
                time1 = Doctor.objects.get(id=did).morningTime
            else:
                # appointments.sort()
                time1 = appointments[len(appointments)-1].time
                time2= str(time1).split(':')
                time1 = datetime.strptime((datetime.timedelta (int(time2[0]), int(time2[1]), 0) + datetime.timedelta(0,15,0)), '%H:%M:%S')
                print (time1)
                # time.strptime(time_string[, format])

            appointment=Appointment()
            print(request.session['pid'])
            appointment.patientId = Patient.objects.get(id = request.session['pid'])
            appointment.doctorId = Doctor.objects.get(id=did)
            appointment.time= time1
            appointment.date = request.POST['date']
            appointment.status = "cancel"
            appointment.save()
            print("app")
            return render(request,'temp.html')
    return render(request,'appointment.html')

def findDoctor(request,dname):
    doctor = list(Doctor.objects.get(doctorName = dname))
    context={}
    context['doctors']=doctor
    print(doctor)
    return render(request,'patientHome.html',context)

def getDoctors(request):
    context={}
    doctors= list(Doctor.objects.all())
    context['doctors']=doctors
    return render(request,'patientHome.html',context)

        