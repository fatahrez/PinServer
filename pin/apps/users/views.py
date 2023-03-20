from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from pin.apps.users.serializers import EmailSerializer


User = get_user_model()

class EmailAPIView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"message": False}, status=status.HTTP_200_OK)
            return Response({"message": True}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)