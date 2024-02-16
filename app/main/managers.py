from django.db import models
from django.db.models.query import QuerySet

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="PB")