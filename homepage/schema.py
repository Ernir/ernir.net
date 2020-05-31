import graphene

from graphene_django.types import DjangoObjectType

from .models import FrontPageSection


class FrontPageSectionType(DjangoObjectType):
    class Meta:
        model = FrontPageSection


class Query(object):
    all_frontpage_sections = graphene.List(FrontPageSectionType)

    def resolve_all_frontpage_sections(self, info, **kwargs):
        return FrontPageSection.objects.all()
