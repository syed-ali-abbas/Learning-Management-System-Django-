from django.views import View
from django.shortcuts import render
from Accounts.models.Students import User
from Accounts.models.category import Categorie




class HomePageView(View):
    def get(self, request):
        id = request.session['student_id']
        if id:
            user = User.get_all_user_data_by_id(id)
            cat = Categorie.get_all_categories()

            data = {
                'stud': user,
                'category':cat
            }
            # return render(request, 'profileView.html', data)
        return render(request, 'home.html',data)