from django.db import models
from .Class import Clas


class Course_upload(models.Model):
    course_name=models.CharField(max_length=100)
    class_name = models.ForeignKey(Clas, on_delete=models.CASCADE, default=None)
    upload_file=models.FileField(upload_to='Course_Outline_Files/uploads')

    @staticmethod
    def get_courses_data_by_id(class_name):
        id = Course_upload.objects.filter(class_name=class_name)
        return id

    def __str__(self):
        return self.course_name

