from django.views import View
from django.shortcuts import render
from Accounts.models.Students import User
from Accounts.models.category import Categorie
from Accounts.models.courses import Course_upload
from Accounts.models.Class import Clas


class CourseOutline(View):
    def get(self, request):
        id = request.session['student_id']
        error_msg = None
        if id:
            user = User.get_all_user_data_by_id(id)
            cat = Categorie.get_all_categories()
            cn = user.program
            class_id = Clas.get_all_Clas_name(cn)
            print(class_id)
            subject_id = Course_upload.get_courses_data_by_id(class_id)
            if not subject_id:
                error_msg = 'No Outline Avaliable'
                data = {
                    'error': error_msg,
                    'stud': user,
                    'category': cat
                }
            else:
                data = {
                    'course_data': subject_id,
                    'stud': user,
                    'category': cat
                }
        return render(request, 'course_outline.html', data)
