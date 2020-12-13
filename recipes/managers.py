from django.db import models


class FullRecipeManager(models.Manager):
    def get_queryset(self):
        return (
            super(FullRecipeManager, self)
            .get_queryset()
            .prefetch_related("ingredients",)
        )
