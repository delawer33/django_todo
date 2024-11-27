from django import forms
from django.contrib.auth.forms import UserCreationForm

from myauth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ('email',)

# class LoginForm(forms.ModelForm):
#     class Meta:
#
#         model = User
#         fields = ('email', 'password')
