from django.contrib import admin

from restaurants import models


@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    readonly_fields = ("updated_at", "created_at")
