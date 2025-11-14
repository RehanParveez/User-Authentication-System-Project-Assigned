from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from user.models import Kaam
from user.forms import KaamForm
from django.contrib.auth.models import User

# Authenticate

class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('login')
    
    

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'
    

class OwnLoginView(View):
    template_name = 'user/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('all_tasks')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, self.template_name)

class OwnLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('own_login')


class AllKaamView(LoginRequiredMixin, ListView):
    model = Kaam
    template_name = 'user/task_list.html'
    context_object_name = 'kaams'
    ordering = ['-created_at']

    def get_queryset(self):
        return Kaam.objects.filter(user=self.request.user).order_by('-created_at')


class AddKaamView(LoginRequiredMixin, CreateView):
    model = Kaam
    form_class = KaamForm
    template_name = 'user/task_form.html'
    success_url = reverse_lazy('all_tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditKaamView(LoginRequiredMixin, UpdateView):
    model = Kaam
    form_class = KaamForm
    template_name = 'user/task_form.html'
    success_url = reverse_lazy('all_tasks')

    def get_queryset(self):
        return Kaam.objects.filter(user=self.request.user)


class RemoveKaamView(LoginRequiredMixin, DeleteView):
    model = Kaam
    template_name = 'user/task_confirm_delete.html'
    success_url = reverse_lazy('all_tasks')

    def get_queryset(self):
        return Kaam.objects.filter(user=self.request.user)

