from django.urls import include, path

urlpatterns = [
    path("allauth", include("allauth.headless.urls")),
]
