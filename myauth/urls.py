from django.urls import path, reverse_lazy
from . import views


app_name = 'myauth'

urlpatterns = [
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]