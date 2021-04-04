from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usersapp'

urlpatterns = [
    path('reset/', views.reset_password, name = "reset-password"),
    path('sign-up/', views.sign_up, name = "sign-up"),
    path('signup/', views.sign_up, name = "sign-up"),
    path('sign-in/', auth_views.LoginView.as_view(template_name='usersapp/sign-in.html'), name = 'sign-in'),
    path('', auth_views.LoginView.as_view(template_name='usersapp/sign-in.html'), name = 'home')
]
