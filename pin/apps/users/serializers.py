from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")
    profile_photo=serializers.ImageField(source="profile.profile_photo")
    country = CountryField(source="profile.country")
    first_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'gender', 
            'country', 
            'profile_photo'
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()
    
    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation
    

class CreateUserSerializer(UserCreateSerializer):
    token = serializers.SerializerMethodField()
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "username",
            "email", 
            "first_name", 
            "password",
            "token"
        ]

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()