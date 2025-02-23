from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import AuthUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = AuthUser
        fields = ["username", "email", "password1", "password1"]
