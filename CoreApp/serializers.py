from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attr): #Validate is a pre defined function that determines what items to return in Json Format..We are over riding that function here.
        x = super(CustomTokenObtainPairSerializer,self).validate(attr) #Super(current_class,self).parent_class's function_name() is syntax of super().This function tells the compiler that we are using parent class's function .. We can also do  -->  = TokenObtainPairSerialzier.validate(attrs)
        obj = str(Group.objects.get(user=self.user))
        x.update({"user_group":obj})
        return x
