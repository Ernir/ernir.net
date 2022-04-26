import os
import time

import googlemaps
import numpy
from django.core.management.base import BaseCommand

from restaurants.models import Restaurant


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.gmaps_client = googlemaps.Client(key=os.environ.get("GOOGLE_MAPS_API_KEY"))
        self.type = "restaurant"
        self.region = "NL"

    def handle(self, *args, **options) -> None:
        # Van Heenvlietlaan = (52.32587853655816, 4.882333537153177)
        northeast = (52.398505, 4.956774)
        southwest = (52.323440, 4.840631)

        northsouth_steps = list(numpy.linspace(52.398505, 52.323440, num=10))
        eastwest_steps = list(numpy.linspace(4.840631, 4.956774, num=10))

        for lat in northsouth_steps[4:]:
            for lng in eastwest_steps:
                self.search_and_upsert((lat, lng))

    def search_and_upsert(self, latlng):
        restaurants = self.find_restaurants(latlng)
        new_count = 0
        for r in restaurants:
            restaurant, created = self.upsert_restaurant(r)
            if created:
                new_count += 1
        print(
            f"Found {len(restaurants)} restaurants near {latlng}, {new_count} new, {len(restaurants) - new_count} already known"
        )

    @staticmethod
    def upsert_restaurant(r):
        if "rating" in r:
            try:
                restaurant = Restaurant.objects.get(google_place_id=r["place_id"])
                restaurant.update_ratings(r["rating"], r["user_ratings_total"])
                return restaurant, False
            except Restaurant.DoesNotExist:
                return (
                    Restaurant.objects.create(
                        name=r["name"],
                        address=r["formatted_address"],
                        location_lat=r["geometry"]["location"]["lat"],
                        location_lng=r["geometry"]["location"]["lng"],
                        google_place_id=r["place_id"],
                        google_rating=r["rating"],
                        google_user_ratings_count=r["user_ratings_total"],
                    ),
                    True,
                )
        else:
            print(f"Warning: Restaurant '{r['name']}' does not have a rating, skipping")
            return None, False

    def find_restaurants(self, latlng, next_page_token=""):
        places = self.gmaps_client.places(
            location=latlng,
            region=self.region,
            type=self.type,
            page_token=next_page_token,
        )
        if "next_page_token" in places:
            # Arbitrary delay allowing Google to apply the next page token serverside
            time.sleep(2)
            return places["results"] + self.find_restaurants(
                latlng, next_page_token=places["next_page_token"]
            )
        else:
            return places["results"]
