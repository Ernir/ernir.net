from django.contrib import admin

from asylum.models import Year, AgeGenderGroup


class AgeGenderGroupInline(admin.TabularInline):
    model = AgeGenderGroup


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    inlines = [AgeGenderGroupInline]
