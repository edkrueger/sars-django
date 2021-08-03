"""Define route logic"""

from django.shortcuts import render


def index(request):
    """Renders home page"""
    return render(request, "index.html")
