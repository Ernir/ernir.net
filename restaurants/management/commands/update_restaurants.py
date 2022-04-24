import os
import time

import googlemaps
from django.core.management.base import BaseCommand

from restaurants.models import Restaurant


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.gmaps_client = googlemaps.Client(key=os.environ.get("GOOGLE_MAPS_API_KEY"))
        self.location = (52.22, 4.53)
        self.type = "restaurant"
        self.region = "NL"

    def handle(self, *args, **options) -> None:
        for restaurant in self.find_restaurants():
            self.upsert_restaurant(restaurant)

    def upsert_restaurant(self, r):
        try:
            restaurant = Restaurant.objects.get(google_place_id=r["place_id"])
            restaurant.update_ratings(r["rating"], r["user_ratings_total"])
        except Restaurant.DoesNotExist:
            Restaurant.objects.create(
                name=r["name"],
                address=r["formatted_address"],
                location_lat=r["geometry"]["location"]["lat"],
                location_lng=r["geometry"]["location"]["lng"],
                google_place_id=r["place_id"],
                google_rating=r["rating"],
                google_user_ratings_count=r["user_ratings_total"],
            )

    def find_restaurants(self, next_page_token=""):
        places = self.gmaps_client.places(
            location=self.location,
            region=self.region,
            type=self.type,
            page_token=next_page_token,
        )
        if "next_page_token" in places:
            # Arbitrary delay allowing Google to apply the next page token serverside
            time.sleep(2)
            return places["results"] + self.find_restaurants(
                next_page_token=places["next_page_token"]
            )
        else:
            return places["results"]
