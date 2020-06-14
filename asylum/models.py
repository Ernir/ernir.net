from django.db import models
from django.forms.models import model_to_dict
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Year(models.Model):
    starting_date = models.DateField(help_text="January 1st of the year in question")
    visible = models.BooleanField(help_text="Whether to expose this year to clients")

    def __str__(self):
        return str(self.starting_date.year)

    class Meta:
        ordering = ("starting_date",)


class Statuses(models.TextChoices):
    GRANTED = "GRANTED", "Asylum granted"
    ADDITIONAL = "ADDITIONAL", "Asylum granted with additional protection"
    HUMANITARIAN = "HUMANITARIAN", "Asylum granted for humanitarian reasons"
    REJECTED = "REJECTED", "Asylum rejected"
    DUBLIN = "DUBLIN", "Dublin regulation deportation"
    GRANTED_ELSEWHERE = "GRANTED_ELSEWHERE", "Asylum granted in another country"
    OTHER = "OTHER", "Other"


class AgeGenderGroup(models.Model):
    men = models.PositiveIntegerField(
        null=True, blank=False, help_text="The number of men in this age-gender group"
    )
    women = models.PositiveIntegerField(
        null=True, blank=False, help_text="The number of women in this age-gender group"
    )
    boys = models.PositiveIntegerField(
        null=True,
        blank=False,
        help_text="The number of non-adult boys in this age-gender group",
    )
    girls = models.PositiveIntegerField(
        null=True,
        blank=False,
        help_text="The number of non-adult girls in this age-gender group",
    )

    status = models.CharField(
        max_length=50,
        choices=Statuses.choices,
        default=Statuses.GRANTED,
        help_text="One of the final states of an asylum application as defined by the Directorate of Immigration",
    )
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(
            model_to_dict(self, fields=("status", "men", "women", "boys", "girls"))
        )

    class Meta:
        unique_together = ("status", "year")


@receiver(post_save, sender=Year)
def pre_populate(sender, instance: Year, **kwargs):
    """
    Pre-populates the year with standard age gender groups
    """
    if not instance.agegendergroup_set.exists():
        for status in Statuses:
            AgeGenderGroup.objects.create(status=status, year=instance)
