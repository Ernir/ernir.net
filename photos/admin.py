from django.contrib import admin

# Register your models here.
from photos import models

admin.site.register(models.Gallery)
admin.site.register(models.Photo)
