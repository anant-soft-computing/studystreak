"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from assessment.views import assessmentListView, assessmentRetUpdDelView
from coursedetail.views import LessonListView, LessionRetUpdDelView
from Courses.views import CourseRetUpdDelView, CourseListView
from live_classes.views import LiveClassListView, LiveClassRetUpdDelView
from master.views import (CategoryListView, CategoryRetUpdDelView, LevelListView, LevelRetUpdDelView, RequirementsListView,
                          RequirementsRetUpdDelView, OutcomesListView, OutcomesRetUpdDelView, LanguageListView, LanguageRetUpdDelView,
                          CourseOverviewListView, CourseOverviewRetUpdDelView, SEOMetakeywordsListView, SEOMetakeywordsRetUpdDelView,
                          PackageTypeListView,PackageTypeRetUpdDelView, CountryListView, CountryRetUpdDelView, StateListView,
                          StateRetUpdDelView, CityListView, CityRetUpdDelView, SectionListView,SectionRetUpdDelView, batchListView, 
                          batchRetUpdDelView)

from package.views import PackageListView, PackageRetUpdDelView
from students.views import *
from website.views import (HomepageSliderListView, HomepageSliderRetUpdDelView, HomepageSection1ListView, 
                           HomepageSection1RetUpdDelView, HomepageSection2ListView, HomepageSection2RetUpdDelViews, BlogListView, BlogRetUpdDelViews)
from Writing_Exam.views import *
from Reading_Exam.views import *
from Listening_Exam.views import *
from Speaking_Exam.views import *
from QuestionBank.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/assessmentview/', assessmentListView.as_view()),
    path('api/assessmentretupddelview/<int:pk>/', assessmentRetUpdDelView.as_view()),
    
    path('api/lssonview/', LessonListView.as_view()),
    path('api/lessionretupddelview/<int:pk>/', LessionRetUpdDelView.as_view()),
    
    path('api/courselistview/', CourseListView.as_view(),),
    path('api/courseretupddelview/<int:pk>/', CourseRetUpdDelView.as_view(),),
    
    # path('api/LiveClassView/', LiveClassView.as_view()),
    path('api/liveclassview/', LiveClassListView.as_view()),
    path('api/liveclassretupddelview/<int:pk>/', LiveClassRetUpdDelView.as_view()),
    
    path('api/categoryview/', CategoryListView.as_view()),
    path('api/categoryretupddelview/<int:pk>/', CategoryRetUpdDelView.as_view()),
    
    
    path('api/levelView/', LevelListView.as_view()),
    path('api/LevelRetUpdDelView/<int:pk>/', LevelRetUpdDelView.as_view()),
    
    path('api/requirementsview/', RequirementsListView.as_view()),
    path('api/requirementsretupddelview/<int:pk>/', RequirementsRetUpdDelView.as_view()),

    
    path('api/outcomesview/', OutcomesListView.as_view()),
    path('api/outcomesretupdelview/<int:pk>/', OutcomesRetUpdDelView.as_view()),
    
    path('api/languageview/', LanguageListView.as_view()),
    path('api/LanguageRetUpdDelView/<int:pk>/', LanguageRetUpdDelView.as_view()),
    
    path('api/courseoverviewview/', CourseOverviewListView.as_view()),
    path('api/courseoverviewretupddelview/<int:pk>/', CourseOverviewRetUpdDelView.as_view()),
    
    path('api/seometakeywordslistview/', SEOMetakeywordsListView.as_view()),
    path('api/seometakeywordsretupddelview/<int:pk>/', SEOMetakeywordsRetUpdDelView.as_view()),
    
    
    path('api/packagetypeview/', PackageTypeListView.as_view()),
    path('api/packagetyperetupddelview/<int:pk>/', PackageTypeRetUpdDelView.as_view()),
    
    path('api/countrylistview/', CountryListView.as_view()),
    path('api/countryretupddelview/<int:pk>/', CountryRetUpdDelView.as_view()),
    
    path('api/statelistview/', StateListView.as_view()),
    path('api/StateRetUpdDelView/<int:pk>/', StateRetUpdDelView.as_view()),

    path('api/citylistview/', CityListView.as_view()),
    path('api/cityretupddelview/<int:pk>/', CityRetUpdDelView.as_view()),
    
    path('api/batchview/', batchListView.as_view()),
    path('api/batchRetUpdDelView/<int:pk>/', batchRetUpdDelView.as_view()),
    
    path('api/sectionlistview/', SectionListView.as_view()),
    path('api/sectionlistview/<int:pk>/', SectionRetUpdDelView.as_view()),
    
    path('api/batchview/', batchListView.as_view()),
    path('api/batchRetUpdDelView/<int:pk>/', batchRetUpdDelView.as_view()),
    
    path('api/packagelistview/', PackageListView.as_view()),
    path('api/packagelistview/<int:pk>/', PackageRetUpdDelView.as_view()),
    
    path('api/homepagesliderlistview/', HomepageSliderListView.as_view()), 
    path('api/HomepageSliderRetUpdDelView/<int:pk>/', HomepageSliderRetUpdDelView.as_view()),
    
    path('api/homepagesection1listview/', HomepageSection1ListView.as_view()), 
    path('api/homepagesliderretupddelview/<int:pk>/', HomepageSection1RetUpdDelView.as_view()),
    
    path('api/homepagesection2listview/', HomepageSection2ListView.as_view()), 
    path('api/homepagesliderretupdde2view/<int:pk>/', HomepageSection2RetUpdDelViews.as_view()),
    
    path('api/blog/', BlogListView.as_view()),
    path('api/blogretupddelview/<int:pk>/', BlogRetUpdDelViews.as_view()),

    path('api/ReadingExam/', ReadingExamListView.as_view()),
    path('api/ReadingExamretupddelview/<int:pk>/', ReadingExamRetUpdDelViews.as_view()),

    path('api/ListeningExam/', ListeningExamListView.as_view()),
    path('api/ListeningExamretupddelview/<int:pk>/', ListeningExamRetUpdDelViews.as_view()),

    path('api/WritingExam/', WritingExamListView.as_view()),
    path('api/WritingExamretupddelview/<int:pk>/', WritingExamRetUpdDelViews.as_view()),

    path('api/SpeakingExam/', SpeakingExamListView.as_view()),
    path('api/SpeakingExamretupddelview/<int:pk>/', SpeakingExamRetUpdDelViews.as_view()),

    path('api/ReadingQuestion/', ReadingQuestionListView.as_view()),
    path('api/ReadingQuestionretupddelview/<int:pk>/', ReadingQuestionRetUpdDelViews.as_view()),

    path('api/ReadingQuestionTypeName/', ReadingQuestionTypeNameListView.as_view()),
    path('api/ReadingQuestionTypeNameretupddelview/<int:pk>/', ReadingQuestionTypeNameRetUpdDelViews.as_view()),

    path('api/ReadingPassageName/', ReadingPassageNameListView.as_view()),
    path('api/ReadingPassageNameretupddelview/<int:pk>/', ReadingPassageNameRetUpdDelViews.as_view()),

    path('api/Reading_Question/', Reading_QuestionListView.as_view()),
    path('api/Reading_Questionretupddelview/<int:pk>/', Reading_QuestionRetUpdDelViews.as_view()),
    
    path('api/ReadingOption/', ReadingOptionListView.as_view()),
    path('api/ReadingOptionretupddelview/<int:pk>/', ReadingOptionRetUpdDelViews.as_view()),
    
    path('api/ListeningQuestion/', ListeningQuestionListView.as_view()),
    path('api/ListeningQuestionretupddelview/<int:pk>/', ListeningQuestionRetUpdDelViews.as_view()), 

    path('api/ListeningQuestionTypeName/', ListeningQuestionTypeNameListView.as_view()),
    path('api/ListeningQuestionTypeNameretupddelview/<int:pk>/', ListeningQuestionTypeNameRetUpdDelViews.as_view()),

    path('api/Listening_Question/', Listening_QuestionListView.as_view()),
    path('api/Listening_Questionretupddelview/<int:pk>/', Listening_QuestionRetUpdDelViews.as_view()),

    path('api/Listening_Options/', Listening_OptionsListView.as_view()),
    path('api/Listening_Optionsretupddelview/<int:pk>/', Listening_OptionsRetUpdDelViews.as_view()),

    path('api/WritingQuestion/', WritingQuestionListView.as_view()),
    path('api/WritingQuestionretupddelview/<int:pk>/', WritingQuestionRetUpdDelViews.as_view()),

    path('api/WritingQuestionType/', WritingQuestionTypeListView.as_view()),
    path('api/WritingQuestionTyperetupddelview/<int:pk>/', WritingQuestionTypeRetUpdDelViews.as_view()),

    path('api/SpeakingQuestion/', SpeakingQuestionListView.as_view()),
    path('api/SpeakingQuestionretupddelview/<int:pk>/', SpeakingQuestionRetUpdDelViews.as_view()),

    path('api/SpeakingQuestionType/', SpeakingQuestionTypeListView.as_view()),
    path('api/SpeakingQuestionTyperetupddelview/<int:pk>/', SpeakingQuestionTypeRetUpdDelViews.as_view()),




]

