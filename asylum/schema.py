import graphene
from django.db.models import Sum
from graphene import ObjectType

from graphene_django.types import DjangoObjectType

from asylum.models import Year, AgeGenderGroup, Statuses

GRANTED_STATUSES = (Statuses.GRANTED, Statuses.ADDITIONAL, Statuses.HUMANITARIAN)


class AgeGenderGroupType(DjangoObjectType):
    """
    A group of asylum seekers, consisting of the four types of people (I know, right?) recognized by the Icelandic Directorate of Immigration: men, women, boys and girls.
    """

    class Meta:
        model = AgeGenderGroup


class AggregateType(ObjectType):
    """
    A view of a group of people, aggregated from multiple `AgeGenderGroupType`s
    """

    men = graphene.Int()
    women = graphene.Int()
    boys = graphene.Int()
    girls = graphene.Int()


class YearType(DjangoObjectType):
    """
    A year of asylum seeker statistics
    """

    year = graphene.Int()

    granted = graphene.Field(
        AggregateType, description="The number of people granted asylum this year"
    )
    not_granted = graphene.Field(
        AggregateType, description="The number of people not granted asylum this year"
    )

    def resolve_year(self: Year, info, **kwargs):
        return self.starting_date.year

    def resolve_granted(self: Year, info, **kwargs):
        return self.agegendergroup_set.filter(status__in=GRANTED_STATUSES).aggregate(
            men=Sum("men"), women=Sum("women"), boys=Sum("boys"), girls=Sum("girls")
        )

    def resolve_not_granted(self: Year, info, **kwargs):
        return self.agegendergroup_set.exclude(status__in=GRANTED_STATUSES).aggregate(
            men=Sum("men"), women=Sum("women"), boys=Sum("boys"), girls=Sum("girls")
        )

    class Meta:
        model = Year


class Query(object):
    years = graphene.List(YearType)
    total_granted = graphene.Field(
        AggregateType, description="The number of all known people granted asylum"
    )
    total_not_granted = graphene.Field(
        AggregateType, description="The number of all known people not granted asylum"
    )

    def resolve_years(self, info, **kwargs):
        return Year.objects.filter(visible=True).all()

    def resolve_total_granted(self, info, **kwargs):
        return AgeGenderGroup.objects.filter(status__in=GRANTED_STATUSES).aggregate(
            men=Sum("men"), women=Sum("women"), boys=Sum("boys"), girls=Sum("girls")
        )

    def resolve_total_not_granted(self, info, **kwargs):
        return AgeGenderGroup.objects.exclude(status__in=GRANTED_STATUSES).aggregate(
            men=Sum("men"), women=Sum("women"), boys=Sum("boys"), girls=Sum("girls")
        )
