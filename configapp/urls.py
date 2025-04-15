# from rest_framework.routers import DefaultRouter
# from django.urls import path,include
#
# from .views import *
# router=DefaultRouter()
# router.register(r'teacher', TeacherViewSet, basename='teacher')
#
#
#
# urlpatterns=[
#
#     path('post_send_otp/', PhoneSendOTP.as_view()),
#     path('post_v_otp/', VerifySMS.as_view()),
#     path('register/', RegisterUserApi.as_view()),
#     path('register/', RegisterUserApi.as_view()),
#     path('student/', StudentApi.as_view()),
#     path('teacher/', TeacherViewSet.as_view()),
#     path('token/', LoginApi.as_view(), name='token_obtain_pair'),
#     path('teacher/create/', TeacherCreateApi.as_view(), name='teacher-create'),
#     path('', include(router.urls)),
#
# ]

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'student', StudentApi, basename='student')

urlpatterns = [
    path('post_send_otp/', PhoneSendOTP.as_view()),
    path('post_v_otp/', VerifySMS.as_view()),
    path('register/', RegisterUserApi.as_view()),  # ✅ faqat bitta marta bo'lishi kerak
    # path('student/', StudentApi.as_view()),
    path('token/', LoginApi.as_view(), name='token_obtain_pair'),
    path('teacher/create/', TeacherCreateApi.as_view(), name='teacher-create'),
    path('', include(router.urls)),  # ✅ teacher/ CRUD endpointlar shu yerda
]

