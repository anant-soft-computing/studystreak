from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from studystreak_api.views import confirm_user
from assessment.views import assessmentListView, assessmentRetUpdDelView
from coursedetail.views import LessionRetUpdDelView, LessonListView
from Courses.views import CourseListView, CourseRetUpdDelView
from exam.views import AnswerViewSet, ExamViewSet, FullLengthTestViewSet
from Listening_Exam.views import ListeningExamListView, ListeningExamRetUpdDelViews
from live_classes.views import LiveClassListView, LiveClassRetUpdDelView
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
)
from studystreak_api.views import redirectview
from package.views import PackageListView, PackageRetUpdDelView
from QuestionBank.views import *  # noqa: F403
from Reading_Exam.views import *  # noqa: F403
from Speaking_Exam.views import *  # noqa: F403
from students.views import *  # noqa: F403
from studystreak_api.views import (
    ChangePasswordView,
    LoginView,
    PasswordResetView,
    ProfileView,
    RegistrationView,
    SendPasswordResetView,
    get_csrf_token,
    SendPasswordResetView,RedirectLinkView, get_csrf_token,
    login_view,
    logout_view,
    set_csrf_token,
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
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("api/li", get_csrf_token, name="csrf-token"),
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("api/login/", LoginView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/assessmentview/", assessmentListView.as_view()),
    path("api/assessmentretupddelview/<int:pk>/", assessmentRetUpdDelView.as_view()),
    path("api/lssonview/", LessonListView.as_view()),
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
    path("api/liveclassview/", LiveClassListView.as_view()),
    path("api/liveclassretupddelview/<int:pk>/", LiveClassRetUpdDelView.as_view()),
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
    path("api/packagetyperetupddelview/<int:pk>/", PackageTypeRetUpdDelView.as_view()),
    path("api/countrylistview/", CountryListView.as_view()),
    path("api/countryretupddelview/<int:pk>/", CountryRetUpdDelView.as_view()),
    path("api/statelistview/", StateListView.as_view()),
    path("api/StateRetUpdDelView/<int:pk>/", StateRetUpdDelView.as_view()),
    path("api/citylistview/", CityListView.as_view()),
    path("api/cityretupddelview/<int:pk>/", CityRetUpdDelView.as_view()),
    path("api/batchview/", batchListView.as_view()),
    path("api/batchRetUpdDelView/<int:pk>/", batchRetUpdDelView.as_view()),
    path("api/sectionlistview/", SectionListView.as_view()),
    path("api/sectionretupddelview/<int:pk>/", SectionRetUpdDelView.as_view()),
    path("api/batchview/", batchListView.as_view()),
    path("api/batchRetUpdDelView/<int:pk>/", batchRetUpdDelView.as_view()),
    path("api/packagelistview/", PackageListView.as_view()),
    path("api/packagelistview/<int:pk>/", PackageRetUpdDelView.as_view()),
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
    path("api/resetpassword/", SendPasswordResetView.as_view(), name="reset-password"),
    path(
        "api/resetpassword/<uid>/<token>/",
        PasswordResetView.as_view(),
        name="reset-with-link",
    ),
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
    path("confirm/<uid>/<token>", confirm_user, name='confirm-user'),
] + router.urls


admin.site.site_header = "StudyStreak Admin"
admin.site.site_header = "StudyStreak"
admin.site.index_title = "StudyStreak"
admin.site.site_title = "StudyStreak adminsitration"
