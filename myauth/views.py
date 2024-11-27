from django import forms
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm



class RegistrationView(CreateView):
    # model = User
    form_class = CustomUserCreationForm
    # fields = ['email', 'username', 'password']
    success_url = reverse_lazy("myauth:login")
    template_name = "myauth/registration.html"


class LoginView(LoginView):
    template_name = "myauth/login.html"
    # form_class = LoginForm
    # success_url = reverse_lazy("app:list")


class LogoutView(LogoutView):
    template_name = "myauth/logout.html"

