from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from django.db import models

from django.contrib.auth import models as auth_models, get_user_model

from individual_project_django_advanced.accounts.managers import AccountUserManager


 # auth_models.AbstractUser


class AccountUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        _("email address"),
        blank=True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = AccountUserManager()

    def __str__(self):
        return self.username


UserModel = get_user_model()


class Profile(models.Model):
    MAX_FIRST_NAME_LEN = 50
    MAX_LAST_NAME_LEN = 50

    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('viewer', 'Viewer'),
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    user_type = models.CharField(
        choices=USER_TYPE_CHOICES,
    )

    first_name = models.CharField(
        _("first name"),
        max_length=MAX_FIRST_NAME_LEN,
        blank=True
    )

    last_name = models.CharField(
        _("last name"),
        max_length=MAX_LAST_NAME_LEN,
        blank=True
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.first_name or self.last_name
