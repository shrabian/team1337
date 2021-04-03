from django.shortcuts import render
from django.http import HttpResponse

def sign_in(request):
    context = {}
    return render(request, 'breakconnect/sign-in.html', context)

def sign_up(request):
    context = {}
    return render(request, 'breakconnect/sign-up.html', context)
    
def reset_password(request):
    context = {}
    return render(request, 'breakconnect/reset-password.html', context)

def start_break(request):
    context = {}
    return render(request, 'breakconnect/start-break.html', context)

def start_chat(request):
    context = {}
    return render(request, 'breakconnect/start-chat.html', context)

def current_chat(request):
    context = {}
    return render(request, 'breakconnect/current-chat.html', context)
