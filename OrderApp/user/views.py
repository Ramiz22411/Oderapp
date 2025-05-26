from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import CustomLoginForm


# Create your views here.
class SignIn(LoginView):
    template_name = 'user/signin.html'
    authentication_form = CustomLoginForm
    success_url = reverse_lazy("advertisements: my-ads")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "Вы уже вошли в систему.")
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class Logout(LogoutView):
    next_page = reverse_lazy("login")


class RegisterView(CreateView):
    template_name = "user/signup.html"
    form_class = BaseUserCreationForm
    success_url = reverse_lazy("login")
