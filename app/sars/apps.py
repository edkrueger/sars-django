"""Holds Config class for the SARS App"""

from django.apps import AppConfig


class SarsConfig(AppConfig):
    """Exposes our SARS app to the central app"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "sars"
