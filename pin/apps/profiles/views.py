from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django_countries import countries

from .models import Profile
from .exceptions import ProfileNotFound
from .serializers import UpdateProfileSerializer


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
    

def country_list(request):
    country_list = [{"name": name, "short_code": code} for code, name in countries]
    return JsonResponse(country_list, safe=False)