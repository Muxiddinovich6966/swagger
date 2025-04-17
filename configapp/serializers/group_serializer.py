
from rest_framework import serializers
from ..models import model_group,model_teacher
from .teacher_serializer import *


class GroupStudentSerializer(serializers.ModelSerializer):

      teacher = TeacherSerializer(read_only=Teacher,many=True)

      class Meta:
          model = GroupStudent
          fields = '__all__'



