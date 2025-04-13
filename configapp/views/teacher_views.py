#
#
# from django.contrib.auth.hashers import make_password
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.contrib.auth.hashers import make_password
# from drf_yasg.utils import swagger_auto_schema
#
# from ..serializers.teacher_serializer import TeacherSerisalizer, TeacherPostSerializer, TeacherUserSerializer
# from ..models import User
#
#
#
#
# class TeacherApi(APIView):
#     @swagger_auto_schema(request_body=TeacherPostSerializer)
#     def post(self, request):
#         data = {"success": True}
#         user_data = request.data['user']
#         teacher_data = request.data['teacher']
#
#         # Avval userni validatsiya qilamiz
#         user_serializer = TeacherUserSerializer(data=user_data)
#         user_serializer.is_valid(raise_exception=True)
#
#         # Parolni hash qilib, flaglarni o‘zgartiramiz
#         validated_user = user_serializer.validated_data
#         validated_user['password'] = make_password(validated_user['password'])
#         validated_user['is_teacher'] = True
#         validated_user['is_active'] = True
#
#         # Userni saqlaymiz
#         user = User.objects.create(**validated_user)
#
#         # Endi teacherga userni biriktiramiz
#         teacher_serializer = TeacherSerisalizer(data=teacher_data)
#         teacher_serializer.is_valid(raise_exception=True)
#
#         teacher = teacher_serializer.save(user=user)
#
#         # Agar ko‘pdan-ko‘p bog‘lanish bo‘lsa, set qilamiz
#         if 'departments' in teacher_data:
#             teacher.departments.set(teacher_data['departments'])
#         if 'course' in teacher_data:
#             teacher.course.set(teacher_data['course'])
#
#         # Javob qaytaramiz
#         data['user'] = TeacherUserSerializer(user).data
#         data['teacher'] = TeacherSerisalizer(teacher).data
#         return Response(data)
#
#
#
#
#from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from ..models import Teacher, User
from ..serializers import TeacherSerializer, TeacherPostSerializer, TeacherUserSerializer


class TeacherApi(APIView):
    # Create (POST) API
    @swagger_auto_schema(request_body=TeacherPostSerializer)
    def post(self, request):
        data = {"success": True}
        user_data = request.data['user']
        teacher_data = request.data['teacher']

        # Userni validatsiya qilish
        user_serializer = TeacherUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)

        # Parolni hash qilish
        validated_user = user_serializer.validated_data
        validated_user['password'] = make_password(validated_user['password'])
        validated_user['is_teacher'] = True
        validated_user['is_active'] = True

        # Userni saqlash
        user = User.objects.create(**validated_user)

        # Teacherga userni biriktirish
        teacher_serializer = TeacherPostSerializer(data=teacher_data)
        teacher_serializer.is_valid(raise_exception=True)

        teacher = teacher_serializer.save(user=user)

        # ManyToMany bog'lanishlari
        if 'departments' in teacher_data:
            teacher.departments.set(teacher_data['departments'])
        if 'course' in teacher_data:
            teacher.course.set(teacher_data['course'])

        # Javob qaytarish
        data['user'] = TeacherSerializer(user).data
        data['teacher'] = TeacherSerializer(teacher).data
        return Response(data, status=status.HTTP_201_CREATED)

    # Read (GET) API
    @swagger_auto_schema(responses={200: TeacherSerializer})
    def get(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({"detail": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(TeacherSerializer(teacher).data)

    # Update (PUT) API
    @swagger_auto_schema(request_body=TeacherPostSerializer)
    def put(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({"detail": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)

        teacher_data = request.data['teacher']
        teacher_serializer = TeacherPostSerializer(teacher, data=teacher_data, partial=True)
        teacher_serializer.is_valid(raise_exception=True)
        teacher_serializer.save()

        # Javob qaytarish
        return Response(teacher_serializer.data)

    # Delete (DELETE) API
    def delete(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({"detail": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)

        teacher.delete()
        return Response({"detail": "Teacher deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
