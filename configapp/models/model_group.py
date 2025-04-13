from .auth_users import *
from .model_teacher import *


class GroupStudent(BaseModel):
    title = models.CharField(max_length=40, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher, related_name='teacher_get')
