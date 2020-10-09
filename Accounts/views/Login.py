from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from Accounts.models.Students import User


class login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        student = User.get_student_by_email(email)
        print(student)
        if student:
            return redirect('home')
        