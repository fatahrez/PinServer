from django.urls import path

from .views import UpdateProfileAPIView

urlpatterns = [
    path(
        "profile/update/<str:username>/",
          UpdateProfileAPIView.as_view(),
          name="update_profile",
        ),
]