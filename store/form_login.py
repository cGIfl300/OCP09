from django import forms
from django.forms import PasswordInput


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(widget=PasswordInput(), label="Password",
                               max_length=100)
