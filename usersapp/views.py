from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

# Create your views here.
def sign_in(request):
    context = {}
    return render(request, 'usersapp/sign-in.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'usersapp/sign-up.html', {'form': form})
    
def reset_password(request):
    context = {}
    return render(request, 'usersapp/reset-password.html', context)