

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *
from .views.group_view import GroupViewSet

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'student', StudentApi, basename='student')
router.register(r'group', GroupViewSet, basename='group')

urlpatterns = [
    path('post_send_otp/', PhoneSendOTP.as_view()),
    path('post_v_otp/', VerifySMS.as_view()),
    path('register/', RegisterUserApi.as_view()),
    # path('student/', StudentApi.as_view()),
    path('token/', LoginApi.as_view(), name='token'),
    path('teacher/create/', TeacherCreateApi.as_view(), name='teacher-create'),
    path('', include(router.urls)),
]

