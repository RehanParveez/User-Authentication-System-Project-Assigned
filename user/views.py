from django.views.generic import CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from user.models import Register
from user.forms import RegisterForm
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
            return redirect('login')
        else:
            messages.error(request, 'invalid username or password')
            return render(request, self.template_name)

class OwnLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
    def post(self, request):
        logout(request)
        return redirect('login')
        


