from django.urls import path
from . import views

app_name = 'breakconnect'

urlpatterns = [
    path('startbreak/', views.start_break, name = "start-break"),
    path('startchat/', views.start_chat, name = "start-chat"),
    path('currentchat/', views.current_chat, name = "current-chat"),
    path('', views.home, name = 'home')
]
