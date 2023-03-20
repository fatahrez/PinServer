from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from .models import Profile

class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = [
            "age",
            "gender",
            "country",
        ]
