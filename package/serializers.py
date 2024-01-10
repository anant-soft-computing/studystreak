from rest_framework import serializers
from .models import Package
from Courses.models import Course
from master.models import Cupon, PackageType
from students.models import Student
class PackageListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
        
class PackageRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
        depth = 1

class CuponCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = ('cupon_name', 'cupon_code', 'campaign_name', 'discount', 'start_date', 'end_date')

class PackageCourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = ('name',)

class CourseCoursePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'Course_Title']

class CoursePackageSerializer(serializers.ModelSerializer):
    packages = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = ['id', 'Course_Title', 'packages'] 

    def get_packages(self, obj):
        return [
            {'package_id': package.id,'package_name': package.package_name, 'package_price': package.package_price, 'soft_copy': package.soft_copy, 
            'hard_copy': package.hard_copy, 'full_length_test': package.full_length_test, 'full_length_test_count': package.full_length_test_count,
            'practice_test': package.practice_test, 'practice_test_count': package.practice_test_count, 'speaking_test': package.speaking_test,
            'speaking_test_count': package.speaking_test_count, 'writing_evaluation': package.writing_evaluation,
            'live_classes_membership':package.live_classes_membership, 'online_membership': package.online_membership, 'offline_membership':package.offline_membership,
            'group_doubt_solving': package.group_doubt_solving, 'group_doubt_solving_count': package.group_doubt_solving_count, 
            'one_to_one_doubt_solving': package.one_to_one_doubt_solving, 'one_to_one_doubt_solving_count': package.one_to_one_doubt_solving_count, 
            'validity': package.validity, 'duration': package.duration, 'coupon_code': CuponCourseSerializer(package.coupon_code).data,
            'PackageType': PackageCourseTypeSerializer(package.PackageType).data,
            'select_course': CourseCoursePackageSerializer(package.select_course).data} 
            for package in obj.package_set.all()]



class CourseListsSerializers(serializers.ModelSerializer):
    # user_profile = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = Package
        fields = ("id","user_package","user_package", "package_name", "package_price", "PackageType", "select_course", "soft_copy", "hard_copy", "full_length_test", 
        "full_length_test_count", "practice_test", "practice_test_count", "speaking_test", "speaking_test_count", "writing_evaluation", 
        "live_classes_membership", "online_membership", "offline_membership", "group_doubt_solving", "group_doubt_solving_count",
        "one_to_one_doubt_solving", "one_to_one_doubt_solving_count", "validity", "duration", "coupon_code", "user_profile")
        depth = 1


class EnrollmentSerializer(serializers.Serializer):
    package_id = serializers.IntegerField()
    batch_id = serializers.IntegerField(required=False)
    course_id = serializers.IntegerField(required=False)

    class Meta:
        model = Package
        fields = ("id","user_package","user_package", "package_name", "package_price", "PackageType", "select_course", "soft_copy", "hard_copy", "full_length_test", 
        "full_length_test_count", "practice_test", "practice_test_count", "speaking_test", "speaking_test_count", "writing_evaluation", 
        "live_classes_membership", "online_membership", "offline_membership", "group_doubt_solving", "group_doubt_solving_count",
        "one_to_one_doubt_solving", "one_to_one_doubt_solving_count", "validity", "duration", "coupon_code", "user_profile")
        depth = 1

# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import UserProfile

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         user_profile = UserProfile.objects.create(user=user)

#         return user