from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import *
router=DefaultRouter()

urlpatterns=[
    path('post_send_otp/', PhoneSendOTP.as_view()),
    path('post_v_otp/', VerifySMS.as_view()),
    path('register/', RegisterUserApi.as_view()),
    path('token/', LoginApi.as_view(), name='token_obtain_pair'),
    path('teacher/create/', TeacherCreateApi.as_view(), name='teacher-create'),

]
