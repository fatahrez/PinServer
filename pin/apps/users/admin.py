from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .forms import CustomUserRegisterForm, CustomUserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    add_form = CustomUserRegisterForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        'pkid', 
        'id',
        'email', 
        'username', 
        'first_name',
        'is_staff', 
        'is_active'
    ]
    list_display_links = [
        'id', 
        'email'
    ]
    list_filter = [
        'email', 
        'username',
        'first_name',
        'is_staff',
        'is_active'
    ]
    fieldsets = (
        (
            _("Login Credentials"),
            {
                'fields': (
                    'email', 
                    'password',
                )
            },
        ),
        (
            _("Personal Information"),
            {
                'fields': (
                    'username', 
                    'first_name',
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                'fields': (
                    'is_staff', 
                    'is_active',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            },
        ),
        (
            _('Important dates'),
            {
                'fields': (
                    'last_login', 
                    'date_joined'
                )
            }
        ),
    )
    add_fieldsets=(
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email', 
                    'password1', 
                    'password2',
                    'is_staff',
                    'is_active',
                ),
            },
        ),
    ),
    search_fields= [
        'email',
        'username',
        'first_name'
    ]


admin.site.register(User, UserAdmin)