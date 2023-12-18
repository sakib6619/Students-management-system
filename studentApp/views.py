import os
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    prof = Student.objects.all()
    return render(request, 'index.html',locals())

def create(request):
    return render(request, 'from.html')

def profileDetails(request,id):
    prof = Student.objects.get(id=id)
    return render(request, 'profileDetails.html',locals())