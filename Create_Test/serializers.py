from rest_framework import serializers, status
from .models import module, createexam
from rest_framework import generics



class createexamserializers(serializers.ModelSerializer):
    class Meta:
        model = createexam
        fields = "__all__"
        depth=2