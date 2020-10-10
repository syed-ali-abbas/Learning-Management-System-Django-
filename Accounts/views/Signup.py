from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from Accounts.models.Students import User
from django.contrib.auth.hashers import make_password


class Signup(View):
    def get(self,request):
        return render(request, 'Signup.html')

    def validation(self,student):
            error_msg = None
            if not student.first_name:
                error_msg = 'First Name is required'
            elif len(student.first_name)<3:
                error_msg='First Name should not be smaller than 3'
            elif not student.last_name:
                error_msg = 'Last Name is required'
            elif len(student.last_name)<3:
                error_msg='last_name should not be smaller than 3'
            elif not student.program:
                error_msg = 'Program is required'
            elif not student.intake_semester:
                error_msg = 'Intake semester is required'
            elif not student.mobile_no:
                error_msg = 'Mobile no. is required'
            elif not student.email:
                error_msg = 'EMail is required'
            elif not student.current_address:
                error_msg = 'Current Address is required'
            elif not student.permanent_address:
                error_msg = 'Permenant Address is required'
            elif not student.Degree_Duration:
                error_msg = 'Degree Duration is required'
            elif not student.max_semester:
                error_msg = 'Maximum Semester is required'
            elif not student.password:
                error_msg = 'Password is required'
            elif len(student.password)<4:
                error_msg='Password should not be smaller than 4'
            elif not student.Image:
                error_msg='Image is required'
            return error_msg




    
    def post(self, request):
        first_name= request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        program= request.POST.get('program')
        intake_semester= request.POST.get('intakesemester')
        mobile_no = request.POST.get('mobilenumber')
        email = request.POST.get('email')
        current_address=request.POST.get('currentaddress')
        permanent_address = request.POST.get('permanentaddress')
        Degree_Duration = request.POST.get('degreeduration')
        max_semester = request.POST.get('maxsemesters')
        password = request.POST.get('password')
        Image = request.POST.get('image')
        
        student = User(first_name=first_name,last_name=last_name,program=program,intake_semester=intake_semester,mobile_no=mobile_no,email=email,current_address=current_address,permanent_address=permanent_address,Degree_Duration=Degree_Duration,max_semester=max_semester,password=password, Image=Image)
        # print(first_name,last_name,program,intake_semester,mobile_no,email,current_address,permanent_address,Degree_Duration,max_semester,password,Image)
        data={
            'firstname':first_name,
            'lastname':last_name,
            'program':program,
            'intakesemester':intake_semester,
            'mobilenumber':mobile_no,
            'email':email,
            'currentaddress':current_address,
            'permanentaddress':permanent_address,
            'degreeduration':Degree_Duration,
            'maxsemesters':max_semester,
            'image':Image
        }
        error_msg = self.validation(student)
        if not error_msg:
            student.password = make_password(student.password)
            student.registeration()
            return redirect('login')
        else:
            print(student.last_name)
            after_error={
                'data_val':data,
                'error_msg':error_msg
            }
            return render(request,'signup.html',after_error)
        
            

       
    

    
