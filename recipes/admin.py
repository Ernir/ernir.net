from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from recipes.models import Recipe, RecipeIngredient, Unit


class IngredientInlineAdmin(admin.TabularInline):
    model = RecipeIngredient


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(MarkdownxModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = (IngredientInlineAdmin,)
