from django.urls import path, include

from django.views import generic as views

urlpatterns = [
    path("", views.TemplateView.as_view(template_name="common/home.html"), name="home"),

]