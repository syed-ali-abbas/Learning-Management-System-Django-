from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=50, blank=True)#
    last_name = models.CharField(max_length=50,blank=True)#
    program=models.CharField(max_length=5,blank=True)#
    year=models.CharField(max_length=15,blank=True)#
    mobile_no = models.CharField(max_length=15, blank=True)#
    email = models.EmailField()#
    current_address=models.CharField(max_length=200,blank=True)#
    permanent_address = models.CharField(max_length=200,blank=True)#
    Degree_Duration = models.CharField(max_length=3,blank=True)#
    max_semester = models.CharField(max_length=15,blank=True)#
    password = models.CharField(max_length=500, blank=True)
    Image=models.ImageField(upload_to='students_image/uploads')
    season = models.CharField(max_length=30, blank=True)




    def get_student_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            False

    
    def registeration(self):
        self.save()

    def __str__(self):
        return self.first_name+"\t"+self.last_name

    @staticmethod
    def get_all_user_data_by_id(id):
        return User.objects.get(id=id)
