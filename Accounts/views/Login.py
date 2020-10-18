from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from Accounts.models.Students import User
from django.contrib.auth.hashers import check_password
from Accounts.models.category import Categorie


class login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        student = User.get_student_by_email(email)
        # print(student)
        error_msg=None
        if student:
            flag = check_password(password, student.password)
            if flag:
                request.session['student_id']=student.id
                categories = Categorie.get_all_categories()
                data = {
                    'category': categories,
                    'stud':student
                }
                # print(categories)
                return render(request,'home.html',data)
            else:
                error_msg='Password Incorrect'
        else:
            error_msg='No user found with this email'
        
        error={
            'error':error_msg
        }
        return render(request,'login.html',error)
        
            
def logout(request):
    request.session.clear()
    return redirect('login')