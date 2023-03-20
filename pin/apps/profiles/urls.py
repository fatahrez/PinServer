from django.urls import path

from .views import UpdateProfileAPIView, country_list

urlpatterns = [
    path(
      "profile/update/<str:username>/",
      UpdateProfileAPIView.as_view(),
      name="update_profile",
    ),
    path("profile/countries/", country_list, name="countries")

]