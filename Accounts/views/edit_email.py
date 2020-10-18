from Accounts.models.Students import User
from django.shortcuts import render
from django.views import View
from Accounts.models.category import Categorie


class UpdateEmail(View):
    def get(self, request):
        user_id = request.session['student_id']
        cat = Categorie.get_all_categories()
        if user_id:
            user = User.get_all_user_data_by_id(user_id)
            data = {
                'student': user,
                'category':cat
            }

        return render(request, 'edit_email.html', data)



    def post(self, request):
        msg=None
        user_id = request.session['student_id']
        email = request.POST.get('email')
        if user_id:
            user = User.get_all_user_data_by_id(user_id)
            user.email = email
        if user.email:
            msg='Email Updated successfully'
            user.registeration()
            data={
                'msg':msg
            }
        return render(request, 'edit_email.html',data)

