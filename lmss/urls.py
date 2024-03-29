from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from assessment.views import assessmentListView, assessmentRetUpdDelView
from coursedetail.views import LessionRetUpdDelView, LessonListView, LessonCreateView
from Courses.views import CourseListView, CourseRetUpdDelView, Course_list_forpackage
from exam.views import AnswerViewSet, ExamViewSet, FullLengthTestViewSet, ExamListView,AnswerListView,ExamListFilterView, AnswerRetUpdDelView, ExamRetUpdDelView
from Listening_Exam.views import ListeningExamListView, ListeningExamRetUpdDelViews
from LiveClass.views import LiveClassListView, LiveClassUsersView, liveclass_list_view, Liveclass_Create_View
from master.views import (
    CategoryListView,
    CategoryRetUpdDelView,
    CityListView,
    CityRetUpdDelView,
    CountryListView,
    CountryRetUpdDelView,
    CourseOverviewListView,
    CourseOverviewRetUpdDelView,
    LanguageListView,
    LanguageRetUpdDelView,
    LevelListView,
    LevelRetUpdDelView,
    OutcomesListView,
    OutcomesRetUpdDelView,
    PackageTypeListView,
    PackageTypeRetUpdDelView,
    QuestionTypeView,
    RequirementsListView,
    RequirementsRetUpdDelView,
    SectionListView,
    SectionRetUpdDelView,
    SEOMetakeywordsListView,
    SEOMetakeywordsRetUpdDelView,
    StateListView,
    StateRetUpdDelView,
    TestTypeViewset,
    batchListView,
    batchRetUpdDelView,
    CountryInterestedListView,
    BatchListByPackageView,
    CourseMaterialListView,
    CourseMaterialRetUpdDelView,
    AdditionalResourceListAPIView,
    LessonAssignmentListAPIView,
    LessonAttachmentListAPIView,
    CuponListView,
    CreateBatchAPIView,
    Live_Class_Type_List_View

)
from package.views import (PackageListView, PackageRetUpdDelView, CoursePackageView, UserWisePackageWithCourseID, 
 EnrollPackageView,EnrollPackageStudentView, PackageCreateView )
from QuestionBank.views import *  # noqa: F403
from Reading_Exam.views import *  # noqa: F403
from Speaking_Exam.views import *  # noqa: F403
from students.views import StudentView, StudentRetUpdDelView, StudentRetUpdDelUserView, Student_List_View_Dashboard
from studystreak_api.views import (
    ChangePasswordView,
    GetUserRole,
    GetUserView,
    LoginView,
    PasswordResetView,
    ProfileView,
    RegistrationView,
    SendPasswordResetView,
    confirm_user,
    get_csrf_token,
    UserResetPasswordView,
    
)
from website.views import (
    BlogListView,
    BlogRetUpdDelViews,
    HomepageSection1ListView,
    HomepageSection1RetUpdDelView,
    HomepageSection2ListView,
    HomepageSection2RetUpdDelViews,
    HomepageSliderListView,
    HomepageSliderRetUpdDelView,
)
from Writing_Exam.views import *  # noqa: F403
from payment.views import start_payment, handle_payment_success
from django.views.generic import TemplateView
from LiveClass.views import liveclass_listwithid_view,StudentLiveClassEnrollmentAPIView, StudentRemoveLiveClassAPIView
from Create_Test.views import createexamview, ResponsesView, moduleListView
from ExamResponses.views import StudentAnswerListView

router = DefaultRouter()
router.register("api/exam-blocks", ExamViewSet, basename="exam-blocks")
router.register(
    "api/exam-blocks-answers", AnswerViewSet, basename="exam-blocks-answers"
)

router.register(
    "api/full-length-test", FullLengthTestViewSet, basename="full-length-test"
)
router.register("api/test-types", TestTypeViewset, basename="test-types")

urlpatterns = [
    path('api/live-classes/', LiveClassListView.as_view(), name='live-classes-list'),
    path('api/live-classes-users/', LiveClassUsersView.as_view(), name='live-classes-users'),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("api/li", get_csrf_token, name="csrf-token"),
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("api/login/", LoginView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/assessmentview/", assessmentListView.as_view()),
    path("api/assessmentretupddelview/<int:pk>/", assessmentRetUpdDelView.as_view()),
    path("api/lessonview/", LessonListView.as_view()),
    path("api/lessionretupddelview/<int:pk>/", LessionRetUpdDelView.as_view()),
    path(
        "api/courselistview/",
        CourseListView.as_view(),
    ),
    path(
        "api/courseretupddelview/<int:pk>/",
        CourseRetUpdDelView.as_view(),
    ),
    # path('api/LiveClassView/', LiveClassView.as_view()),
    # path('api/list-live-classes/', LiveClassListView.as_view(), name='live-class-list'),
    # path("api/liveclassview/", LiveClassListView.as_view()),
    #path("api/liveclassretupddelview/<int:pk>/", LiveClassRetUpdDelView.as_view()),
    path("api/categoryview/", CategoryListView.as_view()),
    path("api/categoryretupddelview/<int:pk>/", CategoryRetUpdDelView.as_view()),
    path("api/levelView/", LevelListView.as_view()),
    path("api/LevelRetUpdDelView/<int:pk>/", LevelRetUpdDelView.as_view()),
    path("api/requirementsview/", RequirementsListView.as_view()),
    path(
        "api/requirementsretupddelview/<int:pk>/", RequirementsRetUpdDelView.as_view()
    ),
    path("api/outcomesview/", OutcomesListView.as_view()),
    path("api/outcomesretupdelview/<int:pk>/", OutcomesRetUpdDelView.as_view()),
    path("api/languageview/", LanguageListView.as_view()),
    path("api/LanguageRetUpdDelView/<int:pk>/", LanguageRetUpdDelView.as_view()),
    path("api/courseoverviewview/", CourseOverviewListView.as_view()),
    path(
        "api/courseoverviewretupddelview/<int:pk>/",
        CourseOverviewRetUpdDelView.as_view(),
    ),
    path("api/seometakeywordslistview/", SEOMetakeywordsListView.as_view()),
    path(
        "api/seometakeywordsretupddelview/<int:pk>/",
        SEOMetakeywordsRetUpdDelView.as_view(),
    ),
    path("api/packagetypeview/", PackageTypeListView.as_view()),
    path("api/packagecreateview/", PackageCreateView.as_view(), name = "package-create"),
    path("api/packagetyperetupddelview/<int:pk>/", PackageTypeRetUpdDelView.as_view()),
    path("api/countrylistview/", CountryListView.as_view()),
    path("api/countryretupddelview/<int:pk>/", CountryRetUpdDelView.as_view()),
    path("api/countryinterestedlistview/", CountryInterestedListView.as_view()),
    path("api/statelistview/", StateListView.as_view()),
    path("api/StateRetUpdDelView/<int:pk>/", StateRetUpdDelView.as_view()),
    path("api/citylistview/", CityListView.as_view()),
    path("api/cityretupddelview/<int:pk>/", CityRetUpdDelView.as_view()),
    path("api/batchview/", batchListView.as_view()),
    path("api/batchRetUpdDelView/<int:pk>/", batchRetUpdDelView.as_view()),
    path("api/sectionlistview/", SectionListView.as_view()),
    path("api/sectionretupddelview/<int:pk>/", SectionRetUpdDelView.as_view()),
    # path("api/batchview/", batchListView.as_view()),
    path("api/batchRetUpdDelView/<int:pk>/", batchRetUpdDelView.as_view()),
    path("api/packagelistview/", PackageListView.as_view()),
    path("api/packageretupddelview/<int:pk>/", PackageRetUpdDelView.as_view()),
    path("api/homepagesliderlistview/", HomepageSliderListView.as_view()),
    path(
        "api/HomepageSliderRetUpdDelView/<int:pk>/",
        HomepageSliderRetUpdDelView.as_view(),
    ),
    path("api/homepagesection1listview/", HomepageSection1ListView.as_view()),
    path(
        "api/homepagesliderretupddelview/<int:pk>/",
        HomepageSection1RetUpdDelView.as_view(),
    ),
    path("api/homepagesection2listview/", HomepageSection2ListView.as_view()),
    path(
        "api/homepagesliderretupdde2view/<int:pk>/",
        HomepageSection2RetUpdDelViews.as_view(),
    ),
    path("api/blog/", BlogListView.as_view()),
    path("api/blogretupddelview/<int:pk>/", BlogRetUpdDelViews.as_view()),
    path("api/ReadingExam/", ReadingExamListView.as_view()),  # noqa: F405
    path("api/ReadingExamretupddelview/<int:pk>/", ReadingExamRetUpdDelViews.as_view()),
    path("api/ListeningExam/", ListeningExamListView.as_view()),
    path(
        "api/ListeningExamretupddelview/<int:pk>/",
        ListeningExamRetUpdDelViews.as_view(),
    ),
    path("api/WritingExam/", WritingExamListView.as_view()),
    path("api/WritingExamretupddelview/<int:pk>/", WritingExamRetUpdDelViews.as_view()),
    path("api/SpeakingExam/", SpeakingExamListView.as_view()),
    path(
        "api/SpeakingExamretupddelview/<int:pk>/", SpeakingExamRetUpdDelViews.as_view()
    ),
    path("api/ReadingQuestion/", ReadingQuestionListView.as_view()),
    path(
        "api/ReadingQuestionretupddelview/<int:pk>/",
        ReadingQuestionRetUpdDelViews.as_view(),
    ),
    path("api/ReadingQuestionTypeName/", ReadingQuestionTypeNameListView.as_view()),
    path(
        "api/ReadingQuestionTypeNameretupddelview/<int:pk>/",
        ReadingQuestionTypeNameRetUpdDelViews.as_view(),
    ),
    path("api/ReadingPassageName/", ReadingPassageNameListView.as_view()),
    path(
        "api/ReadingPassageNameretupddelview/<int:pk>/",
        ReadingPassageNameRetUpdDelViews.as_view(),
    ),
    path("api/Reading_Question/", Reading_QuestionListView.as_view()),
    path(
        "api/Reading_Questionretupddelview/<int:pk>/",
        Reading_QuestionRetUpdDelViews.as_view(),
    ),
    path("api/ReadingOption/", ReadingOptionListView.as_view()),
    path(
        "api/ReadingOptionretupddelview/<int:pk>/",
        ReadingOptionRetUpdDelViews.as_view(),
    ),
    path("api/ListeningQuestion/", ListeningQuestionListView.as_view()),
    path(
        "api/ListeningQuestionretupddelview/<int:pk>/",
        ListeningQuestionRetUpdDelViews.as_view(),
    ),
    path("api/ListeningQuestionTypeName/", ListeningQuestionTypeNameListView.as_view()),
    path(
        "api/ListeningQuestionTypeNameretupddelview/<int:pk>/",
        ListeningQuestionTypeNameRetUpdDelViews.as_view(),
    ),
    path("api/Listening_Question/", Listening_QuestionListView.as_view()),
    path(
        "api/Listening_Questionretupddelview/<int:pk>/",
        Listening_QuestionRetUpdDelViews.as_view(),
    ),
    path("api/Listening_Options/", Listening_OptionsListView.as_view()),
    path(
        "api/Listening_Optionsretupddelview/<int:pk>/",
        Listening_OptionsRetUpdDelViews.as_view(),
    ),
    path("api/WritingQuestion/", WritingQuestionListView.as_view()),
    path(
        "api/WritingQuestionretupddelview/<int:pk>/",
        WritingQuestionRetUpdDelViews.as_view(),
    ),
    path("api/WritingQuestionType/", WritingQuestionTypeListView.as_view()),
    path(
        "api/WritingQuestionTyperetupddelview/<int:pk>/",
        WritingQuestionTypeRetUpdDelViews.as_view(),
    ),
    path("api/SpeakingQuestion/", SpeakingQuestionListView.as_view()),
    path(
        "api/SpeakingQuestionretupddelview/<int:pk>/",
        SpeakingQuestionRetUpdDelViews.as_view(),
    ),
    path("api/SpeakingQuestionType/", SpeakingQuestionTypeListView.as_view()),
    path(
        "api/SpeakingQuestionTyperetupddelview/<int:pk>/",
        SpeakingQuestionTypeRetUpdDelViews.as_view(),
    ),
    path("api/registration/", RegistrationView.as_view(), name="registration"),
    path("api/profile/", ProfileView.as_view(), name="profileview"),
    path("api/changepassword/", ChangePasswordView.as_view(), name="change-password"),

    ########## api send via mail 
    path("api/resetpassword/", SendPasswordResetView.as_view(), name="reset-password"),
    path(
        "api/resetpassword/<uid>/<token>/",
        PasswordResetView.as_view(),
        name="reset-with-link",
    ),

    ########## reset password user id with token 
    path("api/user/resetpassword/<uid>/<token>/", UserResetPasswordView.as_view(), name='password_reset'),
    path("froala_editor/", include("froala_editor.urls")),
    path("api/QuestionType", QuestionTypeView.as_view()),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/confirm/<uid>/<token>", confirm_user, name="confirm-user"),
    path("api/whoami/", GetUserRole.as_view(), name="whoami"),
    path("api/getusers/", GetUserView.as_view(), name="GetUsers"),

    path('api/course/<int:pk>/packages/', CoursePackageView.as_view(), name='course-packages'),
    path('api/userwisepackagewithcourseid/', UserWisePackageWithCourseID.as_view(), name='listofcourse' ),

    path('api/enroll-package/', EnrollPackageView.as_view(), name='enroll-package'),
    path('api/studentview/', StudentView.as_view(), name='studentview'),
    path('api/studentretupddelview/<int:pk>/', StudentRetUpdDelView.as_view(), name='studentretupddelview'),
    path('api/studentretupddeluserview/<int:pk>/', StudentRetUpdDelUserView.as_view(), name='studentretupddelview'),

    path('api/filterbatches/<int:package_id>/', BatchListByPackageView.as_view(), name='filter_batches'),

    path('api/course-materials/<int:course_id>/', CourseMaterialListView.as_view(), name='coursemateriallistview'),

    path('api/additional-resources/<int:course_id>/', AdditionalResourceListAPIView.as_view(), name='additional-resource-list'),

    path('api/lesson-assignments/<int:lesson_id>/', LessonAssignmentListAPIView.as_view(), name='lesson-assignment-list'),
    path('api/lesson-attachments/<int:lesson_id>/', LessonAttachmentListAPIView.as_view(), name='lesson-attachment-list'),

    path('api/enrollpackagestudentview/', EnrollPackageStudentView.as_view(), name='enrollpackagestudentview'),

    path('api/pay/', start_payment, name="payment"),
    path('api/payment/success/', handle_payment_success, name="payment_success"),
    path('api/cuponlistview/', CuponListView.as_view(), name="cuponlistview"),
    path('api/courselistforpackage/', Course_list_forpackage.as_view(), name="courselistforpackage"),
    path('api/create-batch/', CreateBatchAPIView.as_view(), name='create-batch'),
    # path('accounts/google/login/', include('allauth.urls')),
    path('api/liveclass_list_view/', liveclass_list_view.as_view(), name='liveclass_list_view'),
    path('api/liveclass_create_view/', Liveclass_Create_View.as_view(), name='liveclass_create_view'),
    path('api/student_list_view_dashboard/', Student_List_View_Dashboard.as_view(), name='Student_List_view_dashboard'),
    path('api/live_class_type_list_view/', Live_Class_Type_List_View.as_view(), name='live_class_type_list_view'),
    path('api/examlistview/', ExamListView.as_view(), name='examlistview'),
    path('api/examretupddelview/<int:pk>/', ExamRetUpdDelView.as_view(), name='examretupddelview'),

    path('api/examlistfilterview/', ExamListFilterView.as_view(), name='examlistfilterview'),
    path('api/lessoncreateview/', LessonCreateView.as_view(), name='lessoncreateview'),
    # path('api/answerlistview/', AnswerListView.as_view(), name='lessoncreateview'),
    path('api/answerretupddelview/<int:pk>/', AnswerRetUpdDelView.as_view(), name='answerretupddelview'),
    path('api/answerslistview/<int:exam_id>/', AnswerListView.as_view(), name='answer-list'),
    path('api/liveclass_listwithid_view/<int:batch_id>/', liveclass_listwithid_view.as_view(), name='liveclass_listwithid_view'),
    path('api/enroll-students-in-live-class/', StudentLiveClassEnrollmentAPIView.as_view(), name='enroll-live-class'),
    path('api/createexamview/', createexamview.as_view(), name='createexamview'),
    path('api/responsesview/', ResponsesView.as_view(), name='responsesview'),
    path('api/remove-live-class/<int:pk>/', StudentRemoveLiveClassAPIView.as_view(), name='remove-live-class'),
    path('api/studentanswerlistview/', StudentAnswerListView.as_view(), name='studentanswerlistview'),
    path('api/moduleListView/', moduleListView.as_view(), name='moduleListView'),




    # path('accounts/',include('allauth.urls')),
    # path('socialaccount/google',TemplateView.as_view(template_name='socialaccount/google.html'),name='google')



    
    


] + router.urls


admin.site.site_header = "StudyStreak Admin"
admin.site.site_header = "StudyStreak"
admin.site.index_title = "StudyStreak"
admin.site.site_title = "StudyStreak adminsitration"
