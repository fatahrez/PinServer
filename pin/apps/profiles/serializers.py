from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from django_countries.models import Country

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


class CountriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = [
            'id',
            'name'
        ]