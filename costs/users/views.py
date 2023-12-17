from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from costs.users.forms import *
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class LoginPerson(SuccessMessageMixin, LoginView):
    form_class = AuthPersonForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('users:login')
    success_message = 'Вы авторизованы'
    
    def get_success_url(self):
        return self.success_url
    
class CreatePerson(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    form_class = RegisterPersonForm
    success_url = reverse_lazy('users:login')
    success_message = 'Пользователь создан'
    
def logout_user(request):
    logout(request)
    messages.success(request, 'Пользователь вышел')
    return redirect(reverse_lazy('main'))