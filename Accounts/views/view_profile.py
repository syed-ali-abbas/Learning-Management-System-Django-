from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from Accounts.models.Students import User


class ProfilePageView(View):
    def get(self, request):
        id = request.session['student_id']
        # print(id)
        if id:
            user = User.get_all_user_data_by_id(id)

            data = {
                'stud': user
            }
            return render(request, 'profileView.html', data)
        else:
            # print("error Orccured")
            return render(request, 'profileView.html')






