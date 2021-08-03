"""All models for our SARS app"""

from django.db import models


class Record(models.Model):
    """Defines schema for one Record"""

    id = models.IntegerField(primary_key=True, db_index=True)
    date = models.DateField()
    country = models.CharField(max_length=255, db_index=True)
    cases = models.IntegerField()
    deaths = models.IntegerField()
    recoveries = models.IntegerField()
