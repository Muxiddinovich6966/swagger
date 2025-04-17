
from rest_framework import viewsets
from ..models import GroupStudent
from ..serializers import GroupStudentSerializer
from configapp.permissions import IsAdminOrReadPatchOnly


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupStudent.objects.all()
    serializer_class = GroupStudentSerializer
    permission_classes = [IsAdminOrReadPatchOnly]