from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime


class Student(models.Model):
    name = models.CharField(max_length=30)
    classs = models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    roll_number = models.IntegerField()
    gender = models.CharField(max_length=20)
    image = models.ImageField(upload_to='student_images',default='student_images/default.jpg') #No need to give root folder i.e Media.. If say we have only one folder i.e images then just write default-'student.jpg'
    date_of_birth = models.DateField()
    date_joined = models.DateField()
    date_left = models.DateField(blank=True,null=True)
    address = models.CharField(max_length=40)
    parents_name = models.CharField(max_length=40)
    parents_number =ArrayField(models.CharField(max_length=13),null=True,blank=True)
    parents_occupation = models.CharField(max_length=40,null=True,blank=True)
    upgrade_year = models.IntegerField(default=datetime.datetime.now().year)
    def __str__(self):
        return self.name

    def batch(self):
        return self.date_joined.strftime('%Y')
