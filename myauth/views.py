from django import forms
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from django.contrib.auth.forms import UserCreationForm




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ('email',)

class RegistrationView(CreateView):
    # model = User
    form_class = CustomUserCreationForm
    # fields = ['email', 'username', 'password']
    success_url = reverse_lazy("myauth:login")
    template_name = "myauth/registration.html"


class LoginView(LoginView):
    template_name = "myauth/login.html"


class LogoutView(LogoutView):
    template_name = "myauth/logout.html"

