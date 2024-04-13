from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from django.utils.translation import gettext_lazy as _

from individual_project_django_advanced.accounts.models import Profile


UserModel = get_user_model()


class AccountUserCreationForm(auth_forms.UserCreationForm):
    user = None

    def __init__(self, *args, **kwargs):
        super(AccountUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'password1', 'password2', )


class AccountUserLoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True})
    )

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }


class AccountUserChangeForm(auth_forms.UserChangeForm):

    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_picture']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'profile_picture': 'Profile Picture:',
        }
