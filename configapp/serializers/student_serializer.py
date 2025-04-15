

from rest_framework import serializers
from ..models import Student, User
from ..serializers import UserSerializer  # Agar bor bo‘lsa

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'user', 'group', 'descreptions']



class StudentUserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_teacher = serializers.BooleanField(read_only=True)
    is_student = serializers.BooleanField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'phone_number', 'password', 'email', 'is_active', 'is_staff', 'is_admin', 'is_teacher', 'is_student',)



class StudentPostSerializer(serializers.Serializer):
    user = StudentUserSerializer()
    student = StudentSerializer()