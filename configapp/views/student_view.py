from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from ..models import Student, User
from ..serializers import StudentSerializer


class StudentApi(APIView):
    # Create (POST) API
    @swagger_auto_schema(request_body=StudentSerializer)
    def post(self, request):
        data = {"success": True}
        user_data = request.data['user']
        student_data = request.data['student']

        # Userni validatsiya qilish
        user_serializer = StudentSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)

        # Parolni hash qilish
        validated_user = user_serializer.validated_data
        validated_user['password'] = make_password(validated_user['password'])
        validated_user['is_student'] = True
        validated_user['is_active'] = True

        # Userni saqlash
        user = User.objects.create(**validated_user)

        # Studentga userni biriktirish
        student_serializer = StudentSerializer(data=student_data)
        student_serializer.is_valid(raise_exception=True)

        student = student_serializer.save(user=user)

        # ManyToMany bog'lanishlari
        if 'group' in student_data:
            student.group.set(student_data['group'])

        # Javob qaytarish
        data['user'] = StudentSerializer(user).data
        data['student'] = StudentSerializer(student).data
        return Response(data, status=status.HTTP_201_CREATED)

    # Read (GET) API
    @swagger_auto_schema(responses={200: StudentSerializer})
    def get(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(StudentSerializer(student).data)

    # Update (PUT) API
    @swagger_auto_schema(request_body=StudentSerializer)
    def put(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        student_data = request.data['student']
        student_serializer = StudentSerializer(student, data=student_data, partial=True)
        student_serializer.is_valid(raise_exception=True)
        student_serializer.save()

        # Javob qaytarish
        return Response(student_serializer.data)

    # Delete (DELETE) API
    def delete(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response({"detail": "Student deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
