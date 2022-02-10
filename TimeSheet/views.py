from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from TimeSheet.models import Profile

# Create your views here.

class HomeView(TemplateView):
    model = Profile
    template_name = 'templates/home.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})