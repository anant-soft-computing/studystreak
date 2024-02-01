from rest_framework import serializers, status
from .models import module, createexam, Responses
from rest_framework import generics



class createexamserializers(serializers.ModelSerializer):
    class Meta:
        model = createexam
        fields = "__all__"
        depth=2


class ResponsesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Responses
        fields = "__all__"
        depth=2