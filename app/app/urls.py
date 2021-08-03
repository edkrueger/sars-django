"""Registers routes for each app"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("sars.urls")),
    path("admin/", admin.site.urls),
]
