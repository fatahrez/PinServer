from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class CustomUserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['email', 'username', 'first_name']
        error_class = "error"

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name']
        error_class = "error"