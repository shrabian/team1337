from django.urls import path
from . import views

app_name = 'usersapp'

urlpatterns = [
    path('', views.sign_in, name = "sign-in"),
    path('signup/', views.sign_up, name = "sign-up"),
    path('reset/', views.reset_password, name = "reset-password"),
]
