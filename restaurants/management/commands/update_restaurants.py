import os
import time

import googlemaps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.gmaps_client = googlemaps.Client(key=os.environ.get("GOOGLE_MAPS_API_KEY"))
        self.location = (52.22, 4.53)
        self.type = "restaurant"
        self.region = "NL"

    def handle(self, *args, **options) -> None:
        self.find_restaurants()

    def find_restaurants(self, next_page_token=""):
        places = self.gmaps_client.places(
            location=self.location,
            region=self.region,
            type=self.type,
            page_token=next_page_token,
        )
        for place in places["results"]:
            print(place["name"])
        if "next_page_token" in places:
            time.sleep(2)  # Arbitrary
            self.find_restaurants(next_page_token=places["next_page_token"])
