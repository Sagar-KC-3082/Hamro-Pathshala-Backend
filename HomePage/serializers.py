from rest_framework import serializers
from .models import *


class Banner_Image_Serializer(serializers.ModelSerializer):
    class Meta:
         model = Banner_Image
         fields = '__all__'


class Principal_Section_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Principal_Section
        fields = '__all__'


class Notice_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class Marquee_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Marquee
        fields = '__all__'


class Other_Section_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Other_Section
        fields = '__all__'

class About_School_Serializer(serializers.ModelSerializer):
    class Meta:
        model = About_School
        fields = '__all__'
