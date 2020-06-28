from adminsortable.admin import SortableAdmin
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Section


@admin.register(Section)
class SectionAdmin(SortableAdmin, MarkdownxModelAdmin):
    pass
