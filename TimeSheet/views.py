from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from TimeSheet.models import Profile, WorkDay
from TimeSheet.forms import NewUserForm, NewProfileForm, NewWorkDayForm

# Create your views here.


class HomeView(TemplateView):
    model = Profile
    template_name = 'templates/home.html'


class ProfileView(DetailView):
    model = Profile
    template_name = 'templates/account.html'


def time_sheet_view(request):

    template_name = 'templates/timesheet.html'
    context = {}

    fk = request.user.id
    query_results = WorkDay.objects.filter(profile_id=fk)

    context.update({
        'query_results': query_results,
    })

    return render(request, template_name, context)


def delete_view(request, id):

    template_name = 'templates/home.html'
    workday_id = id
    context = {}

    if workday_id:
        print('Deleting: ', workday_id, '...')
        WorkDay.objects.filter(id=workday_id).delete()
        print('Deleted')
    else:
        print('not anywhere')

    context.update({
        'workday_id': workday_id,
    })

    return render(request, template_name, context)


class ReportView(ListView):
    model = Profile
    template_name = 'templates/reports.html'


class WorkDayView(CreateView):
    model = WorkDay
    form_class = NewWorkDayForm
    template_name = 'templates/workday.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super(WorkDayView, self).form_valid(form)


def signup_view(request):

    template_name = 'registration/signup.html'
    context = {}

    if request.method == 'POST':
        user_form = NewUserForm(request.POST)
        profile_form = NewProfileForm(request.POST, request.FILES)

        if all((user_form.is_valid(), profile_form.is_valid())):
            user = user_form.save(commit=False)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse_lazy('login'))
        else:
            user_form = NewUserForm()
            profile_form = NewProfileForm()
    else:
        user_form = NewUserForm()
        profile_form = NewProfileForm()


    context.update({
        'user_form': user_form,
        'profile_form': profile_form,
    })

    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('login')