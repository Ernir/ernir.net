from adminsortable.models import SortableMixin
from django.db import models
from markdownx.models import MarkdownxField


class SectionCategory(models.TextChoices):
    FRONT_PAGE = "FRONT_PAGE", "Front page section"
    PROJECT = "PROJECT", "Project description"


class Section(SortableMixin):
    """
    A general type of Markdown-backed HTML section to be shown on the web
    """

    main_text = MarkdownxField()
    category = models.CharField(
        max_length=50,
        choices=SectionCategory.choices,
        default=SectionCategory.FRONT_PAGE,
        help_text="A type of section, defining where it should be shown",
    )

    # A field the model should be ordered by
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.main_text.split("\n")[0]

    class Meta:
        ordering = ("the_order",)
