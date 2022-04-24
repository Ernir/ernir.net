import graphene

from graphene_django.types import DjangoObjectType

from restaurants.models import Restaurant


class RestaurantType(DjangoObjectType):
    heatmap_weight = graphene.Field(graphene.Float)

    def resolve_heatmap_weight(self, info, **kwargs):
        # Initial attempt: just use the rating as weight
        return self.google_rating

    class Meta:
        model = Restaurant


class Query(object):
    restaurants = graphene.List(RestaurantType)

    def resolve_restaurants(self, info, **kwargs):
        return Restaurant.objects.all()
