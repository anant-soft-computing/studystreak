from rest_framework import serializers
from .models import LiveClass
from rest_framework import generics

class LiveClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveClass
        fields = '__all__'
        
        depth = 2
        
class LiveClassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveClass
        fields = "__all__"
        
class LiveClassRetRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        model = LiveClass
        fields = '__all__'
        
        depth = 2
        