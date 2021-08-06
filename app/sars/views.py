"""Define route logic"""
# pylint: disable=no-member, unused-argument

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from .models import Record


def index(request):
    """Renders home page"""
    return render(request, "index.html")


def get_all_records(request):
    """Gets all records from the database"""
    all_records = Record.objects.all()
    all_records_json = serializers.serialize("json", all_records)

    return HttpResponse(all_records_json)
