from django.contrib import admin

# Register your models here.
from photos import models

admin.site.register(models.Gallery)


@admin.register(models.Photo)
class WordAdmin(admin.ModelAdmin):
    readonly_fields = ("width", "height", "url")
