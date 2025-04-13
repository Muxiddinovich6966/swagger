from .model_group import *
from .model_teacher import *


class Student(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    group = models.ManyToManyField(GroupStudent,related_name='get_student')
    descreptions = models.CharField(max_length=200,blank=True,null=True)


    def __str__(self):
        return self.phone_number