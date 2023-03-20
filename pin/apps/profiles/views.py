from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


from pin.apps.users.models import User

from django_countries.models import Country

from .models import Profile
from .exceptions import ProfileNotFound
from .serializers import UpdateProfileSerializer, CountriesSerializer


class UpdateProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user_name = request.user.username
        if user_name != username:
            raise ProfileNotFound
        
        data = request.data
        serializer = UpdateProfileSerializer(
            instance=request.user.profile, data=data, partial=True
        )

        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CountriesListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CountriesSerializer
    queryset = Country.objects.all()