"""TimeSheetManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from TimeSheet.views import HomeView, logout_view, signup_view #, ProfileView, TimeSheetView#, ReportView
from TimeSheetManagement import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('registration/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('registration/signup/', signup_view, name='signup'),
    path('', RedirectView.as_view(url='/registration/login/')),
    path('logout/', logout_view, name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    # path('timesheet/', TimeSheetView.as_view(), name='timesheet'),
    # path('reports/', ReportView.as_view(), name='report'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
