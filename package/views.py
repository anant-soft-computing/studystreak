from django.shortcuts import render
from .models import Package, UserProfile
from .serializers import PackageListSerializers, PackageRetUpdDelSerializers, CoursePackageSerializer, CourseListsSerializers,EnrollmentSerializer, StudentListSerializers
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

    # def get_queryset(self):
    #     user = self.request.user
    #     return Package.objects.filter(user_package=user)
    
    
class PackageRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageRetUpdDelSerializers
    

#  def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         package_count = queryset.count()  
#         serializer = self.serializer_class(queryset, many=True)
#         data = {
#             'package_count': package_count,
#             'packages': serializer.data,
#         }
#         return Response(data)

class CoursePackageView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursePackageSerializer
   

class UserWisePackageWithCourseID(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentListSerializers

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(user=user)

    def get(self, request):
        queryset = self.get_queryset()
        package_count = queryset.count()  
        serializer = self.serializer_class(queryset, many=True)
        print(serializer)
        data = {
            'package_count': package_count,
            'packages': serializer.data,
        }
        return Response(data)

        
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

################# new code ############

# class EnrollPackageView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         serializer = EnrollmentSerializer(data=request.data)
#         if serializer.is_valid():
#             user = self.request.user

#             try:
#                 student = Student.objects.get(user=user)
#             except Student.DoesNotExist:
#                 return Response(
#                     {"detail": "Student not found for the authenticated user."},
#                     status=status.HTTP_404_NOT_FOUND,
#                 )
#             batch_ids = serializer.validated_data.get("batch_ids", [])
#             batches = batch.objects.filter(pk__in=batch_ids)
#             print(f"User: {user}, Student: {student}, Batch IDs: {batch_ids}")
#             already_enrolled_batches = student.create_batch.filter(pk__in=batch_ids)
#             if already_enrolled_batches.exists():
#                 return Response(
#                     {"detail": f"Batch IDs are already enrolled."},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#             new_batches = batches.exclude(pk__in=already_enrolled_batches)
#             student.create_batch.add(*new_batches)
#             print(f"Batches added to create_batch: {new_batches}")
#             for batch_obj in new_batches:
               
#                 course_obj, created = Course.objects.get_or_create(
#                     name=f"{batch_obj.batch_name} Course"
#                 )
              
#                 package_obj, created = Package.objects.get_or_create(
#                     package_name=f"{batch_obj.batch_name} Package",
#                     select_course=course_obj,
#                 )
#                 batch_obj.add_package = package_obj
#                 batch_obj.save()

#             return Response(
#                 {"detail": f"Successfully enrolled in batches."},
#                 status=status.HTTP_201_CREATED,
#             )

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



######################### code working | ###############################

class EnrollPackageView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user

            try:
                student = Student.objects.get(user=user)
            except Student.DoesNotExist:
                return Response({"detail": "Student not found for the authenticated user."}, status=status.HTTP_404_NOT_FOUND)

            batch_ids = serializer.validated_data.get('batch_ids', [])
            batches = batch.objects.filter(pk__in=batch_ids)
            print(f"User: {user}, Student: {student}, Batch IDs: {batch_ids}")

            already_enrolled_batches = student.create_batch.filter(pk__in=batch_ids)
            if already_enrolled_batches.exists():
                return Response({"detail": f"Batch IDs are already enrolled."},
                                status=status.HTTP_400_BAD_REQUEST)

            new_batches = batches.exclude(pk__in=already_enrolled_batches)
            student.create_batch.add(*new_batches)

            print(f"Batches added to create_batch: {new_batches}")

            return Response({"detail": f"Successfully enrolled  in batches."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
