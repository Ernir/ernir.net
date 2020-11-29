from django.db import models
from markdownx.models import MarkdownxField


class Ingredient(models.Model):
    name = models.CharField(max_length=100, help_text="The name of this ingredient")


class Unit(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the unit of measurement", unique=True)


class IngredientAssignment(models.Model):
    amount = models.PositiveIntegerField()
    unit = models.ForeignKey(Unit, db_index=True, on_delete=models.PROTECT)


class Recipe(models.Model):
    name = models.CharField(max_length=100, help_text="The name of this recipe")
    slug = models.SlugField()
    ingredients = models.ManyToManyField(Ingredient, through=IngredientAssignment)


class InstructionStep(models.Model):
    instruction_text = MarkdownxField()
    recipe = models.ForeignKey(Recipe, db_index=True, on_delete=models.CASCADE)
