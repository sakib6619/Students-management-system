from typing import Any
from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER = (
        ('Male','Male',),
        ('Female','Female',),
        ('Others','Others',),
    )
    RELIGION = (
        ('Islam','Islam',),
        ('Hindu','Hindu',),
        ('Buddha','Buddha',),
        ('Others','Others',),
    )
    BLOOD = (
        ('B+','B+',),
        ('B-','B-',),
        ('A+','A+',),
        ('AB+','AB+',),
        ('AB-','AB-',),
        ('O-','O-',),
        ('O+','O+',),
    )
    SEMESTER = (
        ('1st','1st',),
        ('2nd','2nd',),
        ('3rd','3rd',),
        ('5th','5th',),
        ('6th','6th',),
        ('7th','7th',),
        ('8th','8th',),
    )
    SECTION =(
        ('A','A',),
        ('B','B',),
        ('C','C',),
        ('D','D',),
    )
    SHIFT =(
        ('1st_Shift','1st_Shift'),
        ('2nd_Shift','2nd_Shift'),
    )
    name = models.CharField(max_length=200)
    student_id = models.PositiveIntegerField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    roll = models.PositiveIntegerField()
    academicYear = models.DateField()
    gender = models.CharField(max_length=50, choices=GENDER, default='Male')
    religion = models.CharField(max_length=50, choices=RELIGION, default='Islam')
    blood = models.CharField(max_length=50, choices=BLOOD)
    gpa = models.FloatField()
    age = models.PositiveIntegerField()
    semester = models.CharField(max_length=50, choices=SEMESTER)
    section = models.CharField(max_length=50, choices=SECTION)
    shift = models.CharField(max_length=50, choices=SHIFT)
    image = models.ImageField(upload_to='prof_pc/')
    
    def __str__(self):
        return self.name