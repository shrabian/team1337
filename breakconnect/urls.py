from django.urls import path
from . import views

app_name = 'breakconnect'

urlpatterns = [
    path('', views.sign_in, name = "sign-in"),
    path('signup/', views.sign_up, name = "sign-up"),
    path('reset/', views.reset_password, name = "reset-password"),
    path('startbreak/', views.start_break, name = "start-break"),
    path('startchat/', views.start_chat, name = "start-chat"),
    path('currentchat/', views.current_chat, name = "current-chat"),
]
