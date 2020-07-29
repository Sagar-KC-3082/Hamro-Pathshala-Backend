from rest_framework import serializers

from School_Details.models import ClassWithSection
from .models import *

class Teacher_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SectionClasses_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ClassWithSection
        fields = '__all__'

class Teacher_Partial_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','name','email','date_of_birth','date_of_joining','date_left','address','phone_number']

class Teachers_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','name']