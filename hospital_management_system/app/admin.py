from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Patient)

def _str__(self):
    return self.patient_Name
