from django.urls import path, re_path
from .views import PublicInfo


urlpatterns = [
    path("info/", PublicInfo.as_view(), name="public_info")
]