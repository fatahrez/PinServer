from django.urls import path

from pin.apps.users.views import EmailAPIView

app_name = "users"

urlpatterns = [
    path("email/", EmailAPIView.as_view(), name="email-exists"),
]