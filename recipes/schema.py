import graphene

from graphene_django.types import DjangoObjectType

from recipes.models import Recipe, RecipeIngredient, Unit


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe


class IngredientType(DjangoObjectType):
    class Meta:
        model = RecipeIngredient


class UnitType(DjangoObjectType):
    class Meta:
        model = Unit


class RecipeSearch(graphene.InputObjectType):
    slug = graphene.String(required=True)


class Query(object):
    recipe = graphene.Field(RecipeType, slug=graphene.String())
    recipes = graphene.List(RecipeType)

    def resolve_recipe(self, info, slug):
        return Recipe.full_recipe.get(slug=slug)

    def resolve_recipes(self, info, **kwargs):
        return Recipe.full_recipe.all()
