from rest_framework import serializers
from .models import Package
from Courses.models import Course

class PackageListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

       
        
class PackageRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

        depth = 1


# class CoursePackageSerializer(serializers.ModelSerializer):
#     packages = serializers.SerializerMethodField()

#     class Meta:
#         model = Course
#         fields = ['id', 'Course_Title', 'packages']

#     def get_packages(self, obj):
#         return [package.package_name for package in obj.package_set.all()]
class CoursePackageSerializer(serializers.ModelSerializer):
    packages = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = ['id', 'Course_Title', 'packages'] 

    def get_packages(self, obj):
        return [
            {'package_name': package.package_name, 'package_price': package.package_price} 
            for package in obj.package_set.all()
        ]
