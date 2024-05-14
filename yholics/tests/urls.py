# A dummy urlconf for testing

from django.contrib import admin
from django.urls import include, path

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def _dummy_view(_):
    return Response({'hello': 'world'})


urlpatterns = [
    path("manage/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("auth/", include("allauth.headless.urls")),
    path("dummy", _dummy_view, name="dummy"),
]
