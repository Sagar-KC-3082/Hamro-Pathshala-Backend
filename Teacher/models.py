from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import *



class Teacher(models.Model):
    name = models.CharField(max_length=40,blank = True, null = True)
    address = models.CharField(max_length=50,blank = True, null = True)
    email = models.EmailField(unique=True,blank = True, null = True)
    phone_number = ArrayField(models.CharField(max_length=43),null=True,blank=True,unique=True)#IN POSTMAN give phone_number = 1222112,3443443,etc
    date_of_birth = models.DateField(blank = True, null = True)
    date_of_joining = models.DateField(blank = True, null = True)
    date_left = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=40,blank = True, null = True)
    # class_teacher = models.CharField(max_length=20,blank=True)
    # subject_head = models.CharField(max_length=20,blank=True)

    image = models.ImageField(upload_to='teacher_images',default='teacher_images/default.jpg')

    def __str__(self):
        return self.name
