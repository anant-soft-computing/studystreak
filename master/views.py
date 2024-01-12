from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import (
    Category,
    City,
    Country,
    CourseOverview,
    Language,
    Level,
    Outcomes,
    PackageType,
    QuestionType,
    Requirements,
    Section,
    SEOMetakeywords,
    State,
    TestType,
    batch,
)
from .serializers import (
    CategoryListSerializers,
    CategoryRetUpdDelSerializers,
    CityListSerializers,
    CityRetUpdDelSerializers,
    CountryListSerializers,
    CountryRetUpdDelSerializers,
    CourseOverviewListSerializers,
    CourseOverviewRetUpdDelSerializers,
    LanguageListSerializers,
    LanguageRetUpdDelSerializers,
    LevelListSerializers,
    LevelRetUpdDelSerializers,
    OutcomesListSerializers,
    OutcomesRetUpdDelSerializers,
    PackageTypeListSerializers,
    PackageTypeRetUpdDelSerializers,
    QuestionTypeSerializers,
    RequirementsListSerializers,
    RequirementsRetUpdDelSerializers,
    SectionListSerializers,
    SEOMetakeywordsListSerializers,
    SEOMetakeywordsRetUpdDelSerializers,
    StateListSerializers,
    StateRetUpdDelSerializers,
    TestTypeSerializers,
    batchListSerializers,
    CountryInterestedListSerializers
)

# Create your views here.


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class CategoryRetUpdDelView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRetUpdDelSerializers


class LevelListView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelListSerializers


class LevelRetUpdDelView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelRetUpdDelSerializers


class RequirementsListView(generics.ListCreateAPIView):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsListSerializers


class RequirementsRetUpdDelView(generics.ListCreateAPIView):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsRetUpdDelSerializers


class OutcomesListView(generics.ListCreateAPIView):
    queryset = Outcomes.objects.all()
    serializer_class = OutcomesListSerializers


class OutcomesRetUpdDelView(generics.ListCreateAPIView):
    queryset = Outcomes.objects.all()
    serializer_class = OutcomesRetUpdDelSerializers


class LanguageListView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageListSerializers


class LanguageRetUpdDelView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageRetUpdDelSerializers


class CourseOverviewListView(generics.ListCreateAPIView):
    queryset = CourseOverview.objects.all()
    serializer_class = CourseOverviewListSerializers


class CourseOverviewRetUpdDelView(generics.ListCreateAPIView):
    queryset = CourseOverview.objects.all()
    serializer_class = CourseOverviewRetUpdDelSerializers


class SEOMetakeywordsListView(generics.ListCreateAPIView):
    queryset = SEOMetakeywords.objects.all()
    serializer_class = SEOMetakeywordsListSerializers


class SEOMetakeywordsRetUpdDelView(generics.ListCreateAPIView):
    queryset = SEOMetakeywords.objects.all()
    serializer_class = SEOMetakeywordsRetUpdDelSerializers


class PackageTypeListView(generics.ListCreateAPIView):
    queryset = PackageType.objects.all()
    serializer_class = PackageTypeListSerializers


class PackageTypeRetUpdDelView(generics.ListCreateAPIView):
    queryset = PackageType.objects.all()
    serializer_class = PackageTypeRetUpdDelSerializers


###############################################


class CountryListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializers

class CountryInterestedListView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryInterestedListSerializers

class CountryRetUpdDelView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryRetUpdDelSerializers


class StateListView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateListSerializers


class StateRetUpdDelView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateRetUpdDelSerializers


class CityListView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializers


class CityRetUpdDelView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityRetUpdDelSerializers


class SectionListView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionListSerializers


class SectionRetUpdDelView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionListSerializers


"""############################################"""


class batchListView(generics.ListCreateAPIView):
    queryset = batch.objects.all()
    serializer_class = batchListSerializers


class batchRetUpdDelView(generics.ListCreateAPIView):
    queryset = batch.objects.all()
    serializer_class = batchListSerializers


class QuestionTypeView(generics.ListCreateAPIView):
    serializer_class = QuestionTypeSerializers
    queryset = QuestionType.objects.all()


class TestTypeViewset(ModelViewSet):
    serializer_class = TestTypeSerializers
    queryset = TestType.objects.all()
