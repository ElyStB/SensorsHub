from django.urls import path, include

from individual_project_django_advanced.accounts.views import AccountUserRegisterView, AccountUserLoginView, \
    AccountUserLogoutView, ProfileDetailView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path("register/", AccountUserRegisterView.as_view(), name="register"),
    path("login/", AccountUserLoginView.as_view(), name="login"),
    path("logout/", AccountUserLogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", include([
            path("", ProfileDetailView.as_view(), name="profile details"),
            path("edit/", ProfileEditView.as_view(), name="profile edit"),
            path("delete/", ProfileDeleteView.as_view(), name="profile delete"),
]))
    ]
