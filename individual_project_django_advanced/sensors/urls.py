from django.urls import path, include

from individual_project_django_advanced.sensors import views
from individual_project_django_advanced.sensors.views import SensorCreateView, SensorDetailView, SensorDeleteView, SensorEditView

urlpatterns = [
    path("", views.sensors_data_table, name='sensors data table'),
    path("add/", SensorCreateView.as_view(), name="sensor create"),
    path("<str:username>/sensor/<int:pk>", include([
        path("", SensorDetailView.as_view(), name="sensor detail"),
        path("edit/", SensorEditView.as_view(), name="sensor edit"),
        path("delete/", SensorDeleteView.as_view(), name="sensor delete"),
    ]))

]
