from django.shortcuts import render
from .models import Package, UserProfile
from .serializers import (PackageListSerializers, PackageRetUpdDelSerializers, CoursePackageSerializer,EnrollmentSerializer, StudentListSerializers,
EnrollmentPackageSerializer)
from rest_framework import generics
from Courses.models import Course
from students.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from master.models import batch, CourseMaterial, AdditionalResource,LessonAttachment, LessonAssignment 
from Courses.models import Course 
from package.serializers import PackageListSerializers, PackageListForStudentSerializers, PackageCreateSerializers
from Courses.serializers import CourseListSerializers
from master.serializers import (AdditionalResourceListSerializers, CourseMaterialListSerializers,
LessonAttachmentSerializer,LessonAssignmentSerializer,)
# from coursedetail.models import Quiz_Question, QuizOption
# from coursedetail.serializers import QuizOptionListSerializers, Quiz_QuestionListSerializers

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
   
################### code work ########################

# class UserWisePackageWithCourseID(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = StudentListSerializers 

#     def get_queryset(self):
#         user = self.request.user
#         return Student.objects.filter(user=user)

#     def get(self, request):
#         queryset = self.get_queryset()
#         package_count = queryset.count()
        
#         package_list = []
       
#         for student in queryset:
#             create_batch = student.create_batch.all() if student.create_batch else None

#             if create_batch:
#                 for batch in create_batch:
                  
#                     if batch.add_package:
                       
#                         package = batch.add_package

                      
#                         serialized_package = PackageListForStudentSerializers(package).data

                       
#                         package_list.append({
#                             'student_id': student.id,
#                             'student_name': student.user.username,
#                             'selected_batch': batch.batch_name,
#                             'package': serialized_package,
#                         })
#                     else:
                       
#                         package_list.append({
#                             'student_id': student.id,
#                             'student_name': student.user.username,
#                             'selected_batch': batch.batch_name,
#                             'package': None,
#                         })
#             else:
               
#                 package_list.append({
#                     'student_id': student.id,
#                     'student_name': student.user.username,
#                     'selected_batch': None,
#                     'package': None,
#                 })

#         data = {
#             'package_count': package_count,
#             'student_packages': package_list,
#         }

#         return Response(data)
    
#################### code work ########################

# lession_question_count = Quiz_Question.objects.filter(lession__in = course.lessons.all()).count()
# lession_option_count = QuizOption.objects.filter(lession__in = course.lessions.all()).count()



#######################################################
#################### code work ########################
#######################################################


class UserWisePackageWithCourseID(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentListSerializers

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(user=user)

    def get(self, request):
        queryset = self.get_queryset()
        package_count = queryset.count()

        package_list = []

        for student in queryset:
            select_batch = student.select_batch.all() if student.select_batch else None

            if select_batch:
                for batch in select_batch:
                    if batch.add_package:
                        package = batch.add_package
                        course = package.select_course 

                        serialized_course = CourseListSerializers(course).data
                        serialized_package = PackageListForStudentSerializers(package).data

                        package_list.append({
                            'student_id': student.id,
                            'student_name': student.user.username,
                            'selected_batch': batch.batch_name,
                            'batch_id': batch.id,
                            'course': serialized_course,
                            'package': serialized_package,
                        })
                    else:
                        package_list.append({
                            'student_id': student.id,
                            'student_name': student.user.username,
                            'selected_batch': batch.batch_name,
                            'batch_id': batch.id,
                            'course': None,
                            'package': None,
                        })
            else:
                package_list.append({
                    'student_id': student.id,
                    'student_name': student.user.username,
                    'selected_batch': None,
                    'batch_id': None,
                    'course': None,
                    'package': None,
                })

        data = {
            'package_count': package_count,
            'student_packages': package_list,
        }

        return Response(data)

################# new code ############

# class UserWisePackageWithCourseID(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = StudentListSerializers 

#     def get_queryset(self):
#         user = self.request.user
#         return Student.objects.filter(user=user)

#     def get(self, request):
#         queryset = self.get_queryset()
#         package_count = queryset.count()
        
#         package_list = []
       
#         for student in queryset:
#             create_batch = student.create_batch.all() if student.create_batch else None

#             if create_batch:
#                 for batch in create_batch:
#                     if batch.add_package:
#                         package = batch.add_package
#                         course = package.select_course  # Get the selected course

#                         # Serialize course information
#                         serialized_course = CourseListSerializers(course).data

#                         # Get and serialize CourseMaterial and AdditionalResource data
#                         course_material_data = CourseMaterial.objects.filter(course=course)
#                         additional_resource_data = AdditionalResource.objects.filter(course=course)

#                         serialized_course_material = CourseMaterialListSerializers(course_material_data, many=True).data
#                         serialized_additional_resource = AdditionalResourceListSerializers(additional_resource_data, many=True).data
#                         serialized_package = PackageListForStudentSerializers(package).data

#                         package_list.append({
#                             'student_id': student.id,
#                             'student_name': student.user.username,
#                             'selected_batch': batch.batch_name,
#                             'course': serialized_course,
#                             'course_material': serialized_course_material,
#                             'additional_resources': serialized_additional_resource,
#                             'package': serialized_package,
#                         })
#                     else:
#                         package_list.append({
#                             'student_id': student.id,
#                             'student_name': student.user.username,
#                             'selected_batch': batch.batch_name,
#                             'course': None,
#                             'course_material': None,
#                             'additional_resources': None,
#                             'package': None,
#                         })
#             else:
#                 package_list.append({
#                     'student_id': student.id,
#                     'student_name': student.user.username,
#                     'selected_batch': None,
#                     'course': None,
#                     'course_material': None,
#                     'additional_resources': None,
#                     'package': None,
#                 })

#         data = {
#             'package_count': package_count,
#             'student_packages': package_list,
#         }

#         return Response(data)



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

            already_enrolled_batches = student.select_batch.filter(pk__in=batch_ids)
            if already_enrolled_batches.exists():
                return Response({"detail": f"We are sorry, but you are already enrolled in a batch"},
                                status=status.HTTP_400_BAD_REQUEST)

            new_batches = batches.exclude(pk__in=already_enrolled_batches)
            student.select_batch.add(*new_batches)

            print(f"Batches added to select_batch: {new_batches}")

            return Response({"detail": f"Successfully enrolled  in batches."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########################################################
################### packagewiesewnroll ###################
##########################################################

########### code working without self-study logic

# class EnrollPackageStudentView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         serializer = EnrollmentPackageSerializer(data=request.data)
#         if serializer.is_valid():
#             user = self.request.user

#             try:
#                 student = Student.objects.get(user=user)
#             except Student.DoesNotExist:
#                 return Response(
#                     {"detail": "Student not found for the authenticated user."},
#                     status=status.HTTP_404_NOT_FOUND,
#                 )

#             package_ids = serializer.validated_data.get("package_ids", [])
#             packages = Package.objects.filter(pk__in=package_ids)

#             already_enrolled_packages = student.select_package.filter(
#                 pk__in=package_ids
#             )
#             if already_enrolled_packages.exists():
#                 return Response(
#                     {
#                         "detail": f"We are sorry, but you are already enrolled in a package"
#                     },
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#             new_packages = packages.exclude(pk__in=already_enrolled_packages)
#             student.select_package.add(*new_packages)

#             return Response(
#                 {"detail": f"Successfully enrolled in packages."},
#                 status=status.HTTP_201_CREATED,
#             )

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#################################################################
class PackageCreateView(generics.CreateAPIView):

    queryset = Package.objects.all()
    serializer_class = PackageCreateSerializers
    print(serializer_class)
    print("**")

class EnrollPackageStudentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = EnrollmentPackageSerializer(data=request.data)
        print("****")
        if serializer.is_valid():
            user = self.request.user
            print(user)

            try:
                student = Student.objects.get(user=user)
            except Student.DoesNotExist:
                return Response(
                    {"detail": "Student not found for the authenticated user."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            course_delivery = self.request.data.get("course_delivery")
            if course_delivery == "SELF-STUDY":
                return Response(
                    {"detail": "Self-study courses can be enrolled through this API."},
                    status=status.HTTP_200_OK,
                )

            package_ids = serializer.validated_data.get("package_ids", [])
            packages = Package.objects.filter(pk__in=package_ids)

            already_enrolled_packages = student.select_package.filter(
                pk__in=package_ids
            )
            if already_enrolled_packages.exists():
                return Response(
                    {
                        "detail": f"We are sorry, but you are already enrolled in a package"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            new_packages = packages.exclude(pk__in=already_enrolled_packages)
            student.select_package.add(*new_packages)

            return Response(
                {"detail": f"Successfully enrolled in packages."},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     print(serializer_class)
     
