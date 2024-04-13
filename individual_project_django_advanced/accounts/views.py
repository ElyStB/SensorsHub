from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from individual_project_django_advanced.accounts.forms import AccountUserCreationForm, AccountUserLoginForm, \
    ProfileEditForm
from individual_project_django_advanced.accounts.models import Profile
from individual_project_django_advanced.sensors.models import Sensor

from django.views.generic.edit import UpdateView
from . import forms, models

UserModel = get_user_model()


class AccountUserRegisterView(views.CreateView):
    model = UserModel
    form_class = AccountUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class AccountUserRegisterUpdateView(UpdateView):
    model = models.UserModel
    form_class = forms.AccountUserCreationForm


class AccountUserLoginView(auth_views.LoginView):
    form_class = AccountUserLoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class AccountUserLogoutView(auth_views.LogoutView):
    pass


class ProfileDetailView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'

    def my_sensors(self):
        my_sensors = Sensor.objects.all()
        return my_sensors


# class ProfileCreateView(views.CreateView):
#    model = Profile
#    form_class = AccountUserCreationForm


class ProfileEditView(views.UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'accounts/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user.username

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())
