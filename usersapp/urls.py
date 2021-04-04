from django.urls import path
from . import views

app_name = 'usersapp'

urlpatterns = [
    path('signup/', views.sign_up, name = "sign-up"),
    path('reset/', views.reset_password, name = "reset-password"),
]
