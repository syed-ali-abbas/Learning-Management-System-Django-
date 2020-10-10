from django.urls import path
from .views.Signup import Signup
from .views.Login import login, logout
from .views.home import HomePageView

urlpatterns = [
    path('', login.as_view(), name='login'),
    path('signup',Signup.as_view(), name = 'signup'),
    path('home',HomePageView.as_view(), name='home' ),
    path('logout', logout, name ='logout')
]