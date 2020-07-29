from django.db import models
import datetime

class Grade_Details(models.Model):
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=15)
    subject = models.CharField(max_length=15)
    teacher = models.CharField(max_length=30)
    class Meta:
        unique_together = ('grade','section','subject')
    def __str__(self):
        return self.grade+self.section

class Subject(models.Model):
    subject =  models.CharField(max_length=20,unique=True)
    def __str__(self):
         return self.subject

class Section(models.Model):
    section = models.CharField(max_length=20,unique=True)
    def __str__(self):
         return self.section

class ClassWithSection(models.Model):
    grade = models.CharField(max_length=40)
    section = models.CharField(max_length=20)
    class Meta:
        unique_together = ('grade','section')
    def __str__(self):
        return self.grade+self.section

class Result(models.Model):
    student_id = models.CharField(max_length=10)
    student_name = models.CharField(max_length=30)
    classes = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    roll_number = models.CharField(max_length=4)
    exam_type = models.CharField(max_length=30)
    year = models.IntegerField(null=True,blank=True,default=datetime.datetime.now().year)
    maths = models.CharField(max_length=30,null=True,blank=True)
    english = models.CharField(max_length=30,null=True,blank=True)
    nepali = models.CharField(max_length=30,null=True,blank=True)
    science = models.CharField(max_length=30,null=True,blank=True)
    eph = models.CharField(max_length=30,null=True,blank=True)
    computer = models.CharField(max_length=30,null=True,blank=True)
    optional_maths = models.CharField(max_length=30,null=True,blank=True)
    socialstudies = models.CharField(max_length=30,null=True,blank=True)
    gk = models.CharField(max_length=30,null=True,blank=True)
    total = models.CharField(max_length=30,null=True,blank=True)
    percentage = models.CharField(max_length=30,null=True,blank=True)
    division = models.CharField(max_length=30,null=True,blank=True)
    position = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.student_name
