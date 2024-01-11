from django.shortcuts import render
from .models import Package, UserProfile
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
from master.models import batch  # Replace with the actual import path
from Courses.models import Course 
# Create your views here.

class PackageListView(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageListSerializers

    def get_queryset(self):
        user = self.request.user
        return Package.objects.filter(user_package=user)
    
    
class PackageRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageRetUpdDelSerializers
    
    
class CoursePackageView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursePackageSerializer
   

class UserWisePackageWithCourseID(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PackageListSerializers

    def get_queryset(self):
        user = self.request.user
        return Package.objects.filter(user_package=user)   
       
        
    # 

# class EnrollPackageView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         serializer = EnrollmentSerializer(data=request.data)
#         if serializer.is_valid():
#             package_id = serializer.validated_data['package_id']
#             user = request.user

#             # Check if the user is already enrolled in the package
#             existing_enrollment = Student.objects.filter(user=user, course_to_enroll__id=package_id).first()
#             if existing_enrollment:
#                 return Response({"msg": "User is already enrolled in the package", "student_id": existing_enrollment.id}, status=status.HTTP_200_OK)

#             try:
#                 package = Package.objects.get(id=package_id)
#             except Package.DoesNotExist:
#                 return Response({"error": "Package not found"}, status=status.HTTP_404_NOT_FOUND)

#             # Check if the user has an existing student record
#             student, created = Student.objects.get_or_create(user=user, defaults={'course_to_enroll': package})

#             # If the student record already exists, update the course_to_enroll field
#             if not created:
#                 student.course_to_enroll = package
#                 student.save()

#             return Response({"msg": "Enrollment successful", "student_id": student.id}, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnrollPackageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            package_id = serializer.validated_data['package_id']
            batch_id = serializer.validated_data.get('batch_id')
            course_id = serializer.validated_data.get('course_id')
            user = request.user
            print(user)

            
            existing_enrollment = Student.objects.filter(user=user, course_to_enroll__id=package_id).first()
            if existing_enrollment:
                return Response({"msg": "User is already enrolled in the package", "student_id": existing_enrollment.id}, status=status.HTTP_200_OK)

            try:
                package = Package.objects.get(id=package_id)
            except Package.DoesNotExist:
                return Response({"error": "Package not found"}, status=status.HTTP_404_NOT_FOUND)

            
            student, created = Student.objects.get_or_create(user=user, defaults={'course_to_enroll': package})

          
            if not created:
                student.course_to_enroll = package
                student.save()

          
            if batch_id:
                batch_obj = batch.objects.filter(batchuser=user, id=batch_id).first()
                if batch_obj:
                    student.create_batch = batch_obj
                    student.save()
                else:
                    return Response({"error": "Batch not found"}, status=status.HTTP_404_NOT_FOUND)

           
            if course_id:
                course_obj = Course.objects.filter(primary_instructor=user, id=course_id).first()
                if course_obj:
                    student.create_course = course_obj
                    student.save()
                else:
                    return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

            return Response({"msg": "Enrollment successful", "student_id": student.id}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#       // JavaScript for redirecting after 3 seconds
#       setTimeout(function () {
#         window.location.href = "{{link}}";
#       }, 3000);
#     </script>
#   </body>
# </html>

# <a href="{{ link }}" target="_blank" >