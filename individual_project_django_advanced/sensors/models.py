from django.contrib.auth import get_user_model

from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Sensor(models.Model):
    MIN_LENGTH_SENSOR_ID = 3
    MAX_LENGTH_SENSOR_ID = 10
    MAX_LOCATION_LENGTH = 30

    sensor_id = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=MAX_LENGTH_SENSOR_ID,
        validators=[MinLengthValidator(MIN_LENGTH_SENSOR_ID)],
    )

    data_of_registration = models.DateTimeField(
        auto_now_add=True,
    )
# TODO: neobhodima li e tazi kolona?
    is_register_to_user = models.BooleanField(
        default=False,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name="sensors",
    )
