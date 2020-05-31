from django.contrib import admin

# Register your models here.
from photos import models


@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = ("identifier",)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ("width", "height", "url")
