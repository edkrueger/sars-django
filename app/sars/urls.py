"""Registers all routes for the SARS app"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
