from rest_framework import serializers
from ..models import *
from ..serializers import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','user','descreptions','group']


