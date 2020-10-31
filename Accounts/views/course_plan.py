from django.views import View
from django.shortcuts import render, redirect
from Accounts.models.category import Categorie
from Accounts.models.Students import User
from Accounts.models.term import terms
from Accounts.models.subjects import Subjects


class CoursePlan(View):
    def get(self, request):
        id = request.session['student_id']
        if id:
            user = User.get_all_user_data_by_id(id)
            cat = Categorie.get_all_categories()
            term = terms.get_all_term_values()
            subjects = Subjects.get_all_subjects()
            data = {
                'subjects':subjects,
                'term':term,
                'stud': user,
                'category': cat
            }
            # return render(request, 'profileView.html', data)
        return render(request, 'course_plan.html', data)


    def post(self, request):
        term = request.POST.get('term')
        subject = request.POST.get('subject')

        # data_dict={
        #     'subject':subject,
        #     'term':term
        # }
        # data={
        #     'data':data_dict
        # }
        return redirect('course_plan')
