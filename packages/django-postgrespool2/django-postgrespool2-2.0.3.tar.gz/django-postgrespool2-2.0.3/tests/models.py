from django.db import models
from django.utils import timezone


class DogModel(models.Model):

    name = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
