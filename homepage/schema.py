import graphene

from graphene_django.types import DjangoObjectType

from homepage.models import Section, SectionCategory


class SectionType(DjangoObjectType):
    class Meta:
        model = Section


class SectionCategoryType(graphene.ObjectType):
    name = graphene.String()
    label = graphene.String()


class Query(object):
    categories = graphene.List(SectionCategoryType, category_name=graphene.String())
    sections = graphene.List(SectionType, category=graphene.String())

    def resolve_categories(self, info):
        return SectionCategory

    def resolve_sections(self, info, category):
        return Section.objects.filter(category=category).all()
