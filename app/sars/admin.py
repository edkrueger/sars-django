"""Register models to the admin site"""

from django.contrib import admin

from .models import Record

admin.site.register(Record)
