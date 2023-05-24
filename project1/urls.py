"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from app1.views import homePage,aboutPage, coursePage,enquiryPage, viewEnquiry
from app1.views import updateEnquiry, deleteEnquiry, signupPage, staffPage
from django.contrib.auth.views import PasswordResetView,  PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage),
    path('about/',aboutPage),
    path('course/',coursePage),
    path('enquiry/',enquiryPage),
    path('viewenq/',viewEnquiry),
    path('update/<id>/',updateEnquiry),
    path('delete/<id>/',deleteEnquiry),
    path('signup/',signupPage),
    path('login/',LoginView.as_view(template_name='login.html')),
    path('logout/',LogoutView.as_view(next_page='/')),
    path('staffpage/',staffPage),

    path('resetPassword/',PasswordResetView.as_view(template_name='password_reset.html')),
    path('resetDone/',PasswordResetDoneView.as_view(template_name='done.html'),name='password_reset_done'),
    path('confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='confirm.html'),name='password_reset_confirm'),
    path('complete/',PasswordResetCompleteView.as_view(template_name='complete.html'),name='password_reset_complete')

]
