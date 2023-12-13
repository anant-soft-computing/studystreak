from rest_framework import serializers
from .models import (Category, Level, Requirements, Outcomes, Language, CourseOverview, SEOMetakeywords, PackageType, Country, State,
                     City, Section, batch)

# from .models import 

class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        depth = 1
        
class CategoryRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        depth = 1

class LevelListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
        
class LevelRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
        
        # depth = 1
        
class RequirementsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'
        depth = 1
        
class RequirementsRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'
        depth = 1


class OutcomesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Outcomes
        fields = '__all__'
        

class OutcomesRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Outcomes
        fields = '__all__'
        
    
class LanguageListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
        
class LanguageRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
        
class CourseOverviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseOverview
        fields = '__all__'
        
class CourseOverviewRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseOverview
        fields = '__all__'
        
    
class SEOMetakeywordsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SEOMetakeywords
        fields = '__all__'
        
class SEOMetakeywordsRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = SEOMetakeywords
        fields = '__all__'        

        
class PackageTypeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = '__all__'
        
        
class PackageTypeRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = '__all__'
        
        
class CountryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        
class CountryRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        
    
class StateListSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
        
class StateRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
        
class CityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        
        
class CityRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        
        
class SectionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        
class SectionRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        
###################################################
        
class batchListSerializers(serializers.ModelSerializer):
    class Meta:
        model = batch
        fields = '__all__'
        
        
class batchRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = batch
        fields = '__all__'