from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('singup/', views.signupuser, name='singupuser'),
    path('logout/', views.logoutuser, name='logout'),
    path('login/', views.loginuser, name='loginuser'),
    path('ready/', views.ready, name='ready')
]
