from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from individual_project_django_advanced.sensors.forms import SensorCreateForm
from individual_project_django_advanced.sensors.models import Sensor


class SensorCreateView(views.CreateView):
    model = Sensor
    form_class = SensorCreateForm
    template_name = 'sensors/sensor_create.html'

    def form_valid(self, form):
        sensor = form.save(commit=False)
        sensor.user = self.request.user
        sensor.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.pk})


class SensorDetailView(views.DetailView):
    pass


class SensorEditView(views.UpdateView):
    pass


class SensorDeleteView(views.DeleteView):
    pass


def sensors_data_table(request):
    sensor_data = Sensor.objects.all()

    return render(request, 'sensors/sensors_data_table.html', {'sensor_data': sensor_data})