from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework import generics
import requests, json
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from .models import Live_Class
from .serializers import LiveClassListSerializer, LiveClassCreateSerializer, LiveClassListWithIDSerializer
from master.models import batch
from students.models import Student


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
        
        
class liveclass_list_view(generics.ListAPIView):
    queryset = Live_Class.objects.all()
    serializer_class = LiveClassListSerializer


class Liveclass_Create_View(generics.ListCreateAPIView):
    queryset = Live_Class.objects.all()
    serializer_class = LiveClassCreateSerializer



from django.db.models import Count
from django.shortcuts import get_object_or_404

class liveclass_listwithid_view(generics.ListAPIView):
    serializer_class = LiveClassListWithIDSerializer

    def get_queryset(self):
        batch_id = self.kwargs.get('batch_id')
        batch_instance = get_object_or_404(batch, id=batch_id)
        return Live_Class.objects.filter(select_batch=batch_instance)


from django.db import IntegrityError

class StudentLiveClassEnrollmentAPIView(generics.CreateAPIView):
    serializer_class = LiveClassListSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        print(user)

        if hasattr(user, 'student'):
            student = user.student
            # student = user.student
            print("***")
            live_class = serializer.save()
            print("5545")

            try:
                student.Live_class_enroll.add(live_class)
                student.save()
                print("////")
                return Response({"message": "enrollment success"}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"message": "student already enroll"}, status=status.HTTP_400_BAD_REQUEST)
                print("5545")
        else:
            return Response({"message": "User has no associated student"}, status=status.HTTP_400_BAD_REQUEST)



# class StudentLiveClassEnrollmentAPIView(generics.CreateAPIView):
#     serializer_class = LiveClassListSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         user = self.request.user
#         live_class_name = serializer.validated_data.get('meeting_title')

#         if hasattr(user, 'student'):
#             student = user.student

#             live_class, created = Live_Class.objects.get_or_create(meeting_title=live_class_name)

#             if not created and student.live_class_enroll.filter(id=live_class.id).exists():
#                 return Response({"message": "Student already enrolled in this live class"}, status=status.HTTP_400_BAD_REQUEST)

#             student.live_class_enroll.add(live_class)
#             student.save()
#             return Response({"message": "Enrollment success"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"message": "User has no associated student"}, status=status.HTTP_400_BAD_REQUEST)
            

# class StudentLiveClassEnrollmentAPIView(generics.CreateAPIView):
#     serializer_class = LiveClassListSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         user = self.request.user
#         if not hasattr(user, 'student'):
#             return Response({"message": "User has no associated student"}, status=status.HTTP_400_BAD_REQUEST)

#         student = user.student

#         if 'live_class' not in serializer.validated_data:
#             return Response({"message": "Live class data is not available in the request"}, status=status.HTTP_400_BAD_REQUEST)

#         live_class_data = serializer.validated_data['live_class']

#         try:
#             live_class = Live_Class.objects.get(id=live_class_data['id'])
#         except Live_Class.DoesNotExist:
#             return Response({"message": "Live class not found"}, status=status.HTTP_400_BAD_REQUEST)

#         if student.Live_class_enroll.filter(id=live_class.id).exists():
#             return Response({"message": "Student is already enrolled in this live class"}, status=status.HTTP_400_BAD_REQUEST)

#         student.Live_class_enroll.add(live_class)
#         student.save()

#         return Response({"message": "Enrollment successful"}, status=status.HTTP_201_CREATED)