from rest_framework import serializers
from .models import *


class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class Student_Partial_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','roll_number','name','classs','section','address','parents_name','date_joined','date_of_birth']
