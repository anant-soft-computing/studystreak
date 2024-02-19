from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

import requests, json
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated

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
        params = request.data
        if params.get("start_time"):
            start_time = datetime.strptime(params.get("start_time"), '%Y-%m-%d %H:%M:%S')
        else:
            start_time = datetime.utcnow()
        meeting_data = {
            'topic': params.get("topic", 'My Zoom Meeting scheduled'),
            'type': 2,  # 1 for instant meeting, 2 for scheduled meeting
            'start_time': start_time,
            'duration': params.get("duration", 30),  # Meeting duration in minutes
            'timezone': 'UTC',  # Set your desired timezone
            'user_id': params.get("user_id", "jP0UzREKQdaFADMVsxTRlA")
        }
        meeting_list = client.meeting.create(**meeting_data)
        
        print("meeting_list",meeting_list.json())
        return JsonResponse(data= meeting_list.json(), status=200)
        
        
        