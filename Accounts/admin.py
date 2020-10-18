from django.contrib import admin
from Accounts.models.Students import User
from Accounts.models.category import Categorie
from Accounts.models.courses import Course_upload
from Accounts.models.Class import Clas

admin.site.register(User)
admin.site.register(Categorie)
admin.site.register(Course_upload)
admin.site.register(Clas)
