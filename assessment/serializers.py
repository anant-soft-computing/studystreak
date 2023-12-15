from rest_framework import serializers
from .models import assessment
from django.contrib.auth.models import User

class assessmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = assessment
        fields = '__all__'
        
        depth = 2
        
        
class assessmentRetUpdDelSerializer(serializers.ModelSerializer):
    class Meta:
        model = assessment
        fields = '__all__'
        
        depth = 2
        
############# Login Serializer ############

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email"]


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["username", "password"]


