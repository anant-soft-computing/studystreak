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
from students.serializers import StudentSerializers

class liveclass_listwithid_view(generics.ListAPIView):
    serializer_class = LiveClassListWithIDSerializer

    def get_queryset(self):
        batch_id = self.kwargs.get('batch_id')
        batch_instance = get_object_or_404(batch, id=batch_id)
        return Live_Class.objects.filter(select_batch=batch_instance)


from django.db import IntegrityError
from package.serializers import EnrollmentSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny


################## code work ########################
class StudentLiveClassEnrollmentAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def post(self, request, *args, **kwargs):
        live_class_id = request.data.get('live_class_id')
        student_id = request.data.get('student_id')

        try:
            live_class_instance = Live_Class.objects.get(id=live_class_id)
            student_instance = Student.objects.get(id=student_id)

            # Add the Live_Class instance to the Live_class_enroll field
            student_instance.Live_class_enroll.add(live_class_instance)

            serializer = StudentSerializers(student_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Live_Class.DoesNotExist:
            return Response({"error": "Live_Class not found"}, status=status.HTTP_404_NOT_FOUND)

        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        

########################### new code #################################
# class StudentLiveClassEnrollmentAPIView(generics.UpdateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

#     def post(self, request, *args, **kwargs):
#         live_class_id = request.data.get('live_class_id')
#         student_id = request.data.get('student_id')

#         try:
#             live_class_instance = Live_Class.objects.get(id=live_class_id)
#             student_instance = Student.objects.get(id=student_id)

#             # Check if the student is already enrolled in the live class
#             if live_class_instance in student_instance.Live_class_enroll.all():
#                 return Response({"error": "Student is already enrolled in this Live_Class"}, status=status.HTTP_400_BAD_REQUEST)

#             # Add the Live_Class instance to the Live_class_enroll field
#             student_instance.Live_class_enroll.add(live_class_instance)

#             serializer = StudentSerializers(student_instance)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         except Live_Class.DoesNotExist:
#             return Response({"error": "Live_Class not found"}, status=status.HTTP_404_NOT_FOUND)

#         except Student.DoesNotExist:
#             return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


###########################################################################


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