from django.shortcuts import render
from django.http import HttpResponse

def start_break(request):
    context = {}
    return render(request, 'breakconnect/start-break.html', context)

def start_chat(request):
    context = {}
    return render(request, 'breakconnect/start-chat.html', context)

def current_chat(request):
    context = {}
    return render(request, 'breakconnect/current-chat.html', context)

def home(request):
    context = {}
    return render(request, 'breakconnect/start-chat.html', context)
