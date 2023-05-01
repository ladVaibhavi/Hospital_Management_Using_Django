from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
urlpatterns=[
    path('register/',views.registration,name='register'),
    path('addHospital/',views.addHospital,name='addHospital'),
    path('addPatient/',views.addPatient,name='addPatient'),
    path('addDoctor/',views.addDoctor,name='addDoctor'),
    path('loginH/',views.loginHospital,name='loginH'),
    path('loginP/',views.loginPatient,name = 'loginP'),
    path('addAppointment/<did>',views.addAppointment,name='addAppointment'),
    path('findDoctor/<dname>',views.findDoctor,name='findDoctor'),
    path('phome/',views.getDoctors,name='getDoctors')
]