from adminsortable.models import SortableMixin
from django.db import models
from markdownx.models import MarkdownxField


class FrontPageSection(SortableMixin):
    main_text = MarkdownxField()

    # A field the model should be ordered by
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.main_text.split("\n")[0]

    class Meta:
        ordering = ("the_order",)
