from django.db import models


class Restaurant(models.Model):
    place_id = models.CharField(max_length=200, unique=True)
