from django.db import models


class terms(models.Model):
    year = models.CharField(max_length=4, blank=True)
    season = models.CharField(max_length=30)



    def __str__(self):
        return self.year +"\t"+ self.season


    def get_all_term_values():
        return terms.objects.all()