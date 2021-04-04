from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    orgcode = forms.CharField(label="orgcode")
    fullname = forms.CharField(label="fullname")

    class Meta:
        model = User
        fields = ['fullname', 'email', 'orgcode', 'password1', 'password2']

    def save(self, request):
        user = super(UserRegisterForm, self).save(request)
        first_name, last_name = self.cleaned_data["fullname"].split()
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]
        user.organisation_code = self.cleaned_data["orgcode"]
        user.save()
        return user
