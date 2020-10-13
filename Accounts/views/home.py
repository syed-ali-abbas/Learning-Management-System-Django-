from django.views import View
from django.shortcuts import render
from Accounts.models.category import Categorie


class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')