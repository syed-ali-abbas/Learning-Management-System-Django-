from django.db import models

class Categorie(models.Model):
    cat_name = models.CharField(max_length=50)



    @staticmethod
    def get_all_categories():
        return Categorie.objects.all()

    def __str__(self):
        return self.cat_name