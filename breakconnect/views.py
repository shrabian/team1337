from django.shortcuts import render
from django.http import HttpResponse

users = [
    {
        'email': 'person1@email.com',
        'password': 'password',
        'nameFamily': 'Smith',
        'nameGiven': 'Mary',
        'gender': 'Female',
        'yearBorn': '1990'
    },
    {
        'email': 'person2@email.com',
        'password': 'password',
        'nameFamily': 'Smith',
        'nameGiven': 'Mark',
        'gender': 'Male',
        'yearBorn': '1992'
    },
    {
        'email': 'person3@email.com',
        'password': 'password',
        'nameFamily': 'Smith',
        'nameGiven': 'Tom',
        'gender': 'Male',
        'yearBorn': '1995'
    }
]

def sign_in(request):
    context = {}
    return render(request, 'breakconnect/sign-in.html', context)