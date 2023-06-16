from django.shortcuts import render,redirect
from app.models import Patient

def BASE(request):
    return render(request,'base.html')


def ADD_PATIENT(request):
    if request.method=="POST":
        patient_name = request.POST.get('patient_name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        patient = Patient(
            patient_name = patient_name,
            Date_of_birth = dob,
            age = age ,
            phone = phone,
            email = email,
            gender = gender,

        )

        patient.save()

        print(patient_name,dob,age,phone,email,gender,address)


    return render(request,'patients/add_patients.html')