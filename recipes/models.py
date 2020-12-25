from django.db import models
from markdownx.models import MarkdownxField

from recipes.managers import FullRecipeManager


class Recipe(models.Model):
    name = models.CharField(max_length=100, help_text="The name of this recipe")
    slug = models.SlugField()
    description = models.CharField(
        max_length=280,
        help_text="A more extended introduction to what this recipe is all about",
    )
    instruction_text = MarkdownxField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)

    full_recipe = FullRecipeManager()


class Unit(models.Model):
    name = models.CharField(
        max_length=100, help_text="The name of the unit of measurement", unique=True
    )

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients"
    )
    name = models.CharField(max_length=100, help_text="The name of this ingredient")
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    unit = models.ForeignKey(
        Unit, db_index=True, to_field="name", on_delete=models.CASCADE, default="stk"
    )

    def __str__(self):
        return self.name
