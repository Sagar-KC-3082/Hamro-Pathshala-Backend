from rest_framework import serializers
from .models import *


class Assign_TeacherToClass_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Details
        fields = '__all__'


class Subject_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class Section_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class Result_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'