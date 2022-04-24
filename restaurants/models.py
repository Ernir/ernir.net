from django.utils import timezone

from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    location_lat = models.FloatField()
    location_lng = models.FloatField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    google_place_id = models.CharField(max_length=200, unique=True)
    google_rating = models.FloatField()
    google_user_ratings_count = models.IntegerField()

    def __str__(self):
        return self.name

    def update_ratings(self, rating, ratings_count):
        self.google_rating = rating
        self.google_user_ratings_count = ratings_count
        self.updated_at = timezone.now()
        self.save()
