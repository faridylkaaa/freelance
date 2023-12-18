from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from costs.spending.forms import *
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from costs.users.mixins import RightUserMixin
from costs.spending.mixins import AuthorAccessMixin
from costs.spending.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from costs.spending.filters import LeadEntriesFilter

class SpendingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('users:login')
    success_message = 'Трата добавлена'
    template_name = 'spending/create.html'
    form_class = SpendingCreateForm
    success_url = reverse_lazy('spending:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class SpendingUpdateView(AuthorAccessMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    success_message = 'Трата изменена'
    template_name = 'spending/update.html'
    form_class = SpendingCreateForm
    success_url = reverse_lazy('spending:index')
    model = Spending
    
class SpendingDeleteView(AuthorAccessMixin, SuccessMessageMixin, DeleteView):
    model = Spending
    template_name = 'spending/delete.html'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('spending:index')
    success_message = 'Трата удалена'
    
class IndexSpendingsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    def get(self, request, *args, **kwargs):
        f = LeadEntriesFilter(request.GET, queryset=Spending.objects.filter(author=request.user))
        return render(request, 'spending/index.html', {'f': f})