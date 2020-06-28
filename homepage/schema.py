import graphene

from graphene_django.types import DjangoObjectType

from homepage.models import Section, SectionCategory


class SectionType(DjangoObjectType):
    class Meta:
        model = Section


class Query(object):
    all_frontpage_sections = graphene.List(SectionType)

    def resolve_all_frontpage_sections(self, info, **kwargs):
        return Section.objects.filter(category=SectionCategory.FRONT_PAGE).all()
