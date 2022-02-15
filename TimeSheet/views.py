from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from TimeSheet.models import Profile, WorkDay

# Create your views here.


class HomeView(TemplateView):
    model = Profile
    template_name = 'templates/home.html'


# class ProfileView(DetailView):
#     model = Profile
#     template_name = 'templates/account.html'
#
#
# class TimeSheetView(ListView):
#     model = WorkDay
#     template_name = 'templates/timesheet.html'
#
#
# class ReportView(ListView):
#     model = Profile
#     tempalte_name = 'templates/account.html'


class Signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')