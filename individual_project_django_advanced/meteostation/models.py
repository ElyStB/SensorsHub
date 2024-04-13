from django.db import models

from individual_project_django_advanced.sensors.models import Sensor


# Create your models here.
class TemperatureReading(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
    )

    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.sensor.sensor_id} - {self.temperature}C"
