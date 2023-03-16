from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from pin.apps.common.models import TimestampedUUIDModel

User = get_user_model()

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(TimestampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile",
                                on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name=_("Age"), default=20)
    gender = models.CharField(verbose_name=_("Gender"), max_length=20, 
                              choices=Gender.choices, default=Gender.OTHER)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"),
                                      default="/profile_default.png")
    country = CountryField(verbose_name=_("Country"), default="KE",
                           blank=False, null=False)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
