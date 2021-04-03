from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name = "breakconnect-sign-in"),
    path('signup/', views.sign_up, name = "breakconnect-sign-up"),
    path('reset/', views.reset_password, name = "breakconnect-reset-password"),
    path('startbreak/', views.start_break, name = "breakconnect-about"),
    path('startchat/', views.start_chat, name = "breakconnect-about"),
    path('currentchat/', views.current_chat, name = "breakconnect-about"),
]
