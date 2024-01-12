from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']

class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
        depth = 1

class StudentRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1

   