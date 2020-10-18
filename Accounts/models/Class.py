from django.db import models

class Clas(models.Model):
    class_name = models.CharField(max_length=6)




    def get_all_Clas_name(class_name):
        class_name = Clas.objects.get(class_name=class_name)
        return class_name.id

    def __str__(self):
        return self.class_name