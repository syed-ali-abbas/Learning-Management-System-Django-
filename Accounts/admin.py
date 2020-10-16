from django.contrib import admin
from Accounts.models.Students import User
from Accounts.models.category import Categorie


admin.site.register(User)
admin.site.register(Categorie)
