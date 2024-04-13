from django import forms
from individual_project_django_advanced.sensors.models import Sensor


class SensorBaseForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ('sensor_id', 'location', )

        widgets = {
            'sensor_id': forms.TextInput(attrs={'placeholder': 'Sensor ID'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
        }

        labels = {
            'sensor_id': 'Sensor ID',
            'location': 'Location',
        }


class SensorCreateForm(SensorBaseForm):
    pass


class SensorEditForm(SensorBaseForm):
    pass


class SensorDeleteForm(SensorBaseForm):
    pass
