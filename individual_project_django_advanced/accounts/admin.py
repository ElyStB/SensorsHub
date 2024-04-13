from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from individual_project_django_advanced.accounts.forms import AccountUserCreationForm, AccountUserChangeForm

UserModel = get_user_model()


@admin.register(UserModel)
class AccountUserAdmin(auth_admin.UserAdmin):
    model = UserModel
    add_form = AccountUserCreationForm
    form = AccountUserChangeForm

    list_display = ('pk', 'username', 'is_staff', 'is_superuser')
    search_fields = ('username',)
    ordering = ('pk', )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ("first_name", "last_name", "email")}),
        ('Permissions', {'fields': ('is_activ', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )


