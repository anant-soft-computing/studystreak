from django.shortcuts import render
from .models import Package
from .serializers import PackageListSerializers, PackageRetUpdDelSerializers, CoursePackageSerializer, CourseListsSerializers,EnrollmentSerializer
from rest_framework import generics
from Courses.models import Course
from students.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class PackageListView(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageListSerializers
    
    
class PackageRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageRetUpdDelSerializers
    
    
class CoursePackageView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursePackageSerializer
   

class ListofCourse(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = CourseListsSerializers



class EnrollPackageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(f"User: {request.user}")
        
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            package_id = serializer.validated_data['package_id']
            user = request.user

           
            existing_enrollment = Student.objects.filter(user=user, course_to_enroll__id=package_id).first()

            if existing_enrollment:
               
                return Response({"msg": "User is already enrolled in the package", "student_id": existing_enrollment.id}, status=status.HTTP_200_OK)

            try:
                package = Package.objects.get(id=package_id)
            except Package.DoesNotExist:
                print("4444")
                return Response({"error": "Package not found"}, status=status.HTTP_404_NOT_FOUND)

            student = Student.objects.create(user=user, course_to_enroll=package)

            return Response({"msg": "Enrollment successful", "student_id": student.id}, status=status.HTTP_201_CREATED)

        print("7777")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)