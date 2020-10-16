from Accounts.models.Students import User
from django.shortcuts import render
from django.views import View



class UpdateEmail(View):
    def get(self, request):
        return render(request,'edit_email.html')




    def post(self,request):
        user_id = request.session['student_id']
        email = request

        if user_id:
            user = User.get_all_user_data_by_id(user_id)
            student = User(email=email)
            print(user.email)
            data ={
                'student':user
            }
        return render(request,'edit_email.html',data)

