from django.urls import path
from .views.Signup import Signup
from .views.Login import login, logout
from .views.home import HomePageView
from .views.view_profile import ProfilePageView
from Accounts.models.category import Categorie
from .views.edit_email import UpdateEmail
from .views.course_outline import CourseOutline
from .views.course_plan import CoursePlan

urlpatterns = [
    path('', login.as_view(), name='login'),
    path('signup',Signup.as_view(), name = 'signup'),
    path('home',HomePageView.as_view(), name='home' ),
    path('logout', logout, name ='logout'),
    path('category/2/',ProfilePageView.as_view(), name='profileview'),
    path('edit-email',UpdateEmail.as_view(),name='edit_email' ),
    path('category/3/', CourseOutline.as_view(),name='course_outline' ),
    path('category/4/',CoursePlan.as_view(),name='course_plan'),

]