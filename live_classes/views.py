from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework import generics
import requests, json
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from .models import LiveClass
from .serializers import LiveClassListSerializer, LiveClassCreateSerializer,LiveClassListWithIDSerializer
from django.shortcuts import get_object_or_404
from master.models import batch
from zoomus import ZoomClient

Account_id = "gZOcFtX-S3GRietpBWVT-Q"
client_id='vy_n2AFIQJyEIF_4d8g9A'
client_secret='kdxcpDLmMyj4QZcOawul86ktHJm7bMVv'
client = ZoomClient(client_id, client_secret, Account_id)

class LiveClassUsersView(APIView):
    def get(self, request):
        user_list_response = client.user.list()
        user_list = json.loads(user_list_response.content)
        return JsonResponse( data=user_list, status= 200)
    
class LiveClassListView(APIView):
    def get(self, request):
        list_meeting = client.meeting.list(user_id="jP0UzREKQdaFADMVsxTRlA")
        return JsonResponse(data=list_meeting.json(), status =200)
    
    def post(self, request):
        meeting_list = client.meeting.create(user_id="jP0UzREKQdaFADMVsxTRlA", json={
            'topic': 'My Zoom Meeting 1',
            'type': 1,  # 1 for instant meeting, 2 for scheduled meeting
            'password': 'YourMeetingPassword12345'
        })
        print("meeting_list",meeting_list.json())
        return JsonResponse(data= meeting_list.json(), status=200)
        
        
# class liveclass_list_view(generics.ListAPIView):
#     queryset = LiveClass.objects.all()
#     serializer_class = LiveClassListSerializer


# class Liveclass_Create_View(generics.ListCreateAPIView):
#     queryset = LiveClass.objects.all()
#     serializer_class = LiveClassCreateSerializer
    
    

