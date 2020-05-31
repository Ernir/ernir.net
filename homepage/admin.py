from adminsortable.admin import SortableAdmin
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import FrontPageSection


@admin.register(FrontPageSection)
class FrontPageAdmin(SortableAdmin, MarkdownxModelAdmin):
    pass
