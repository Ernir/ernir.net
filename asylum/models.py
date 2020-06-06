from django.db import models
from django.forms.models import model_to_dict
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Year(models.Model):
    # January 1st of the year in question
    starting_date = models.DateField()

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
    """
    A group of asylum seekers, consisting of the four types of people (I know, right?) recognized by the Icelandic Directorate of Immigration: men, women, boys and girls.
    """

    men = models.PositiveIntegerField(null=True, blank=False)
    women = models.PositiveIntegerField(null=True, blank=False)
    boys = models.PositiveIntegerField(null=True, blank=False)
    girls = models.PositiveIntegerField(null=True, blank=False)

    status = models.CharField(
        max_length=50, choices=Statuses.choices, default=Statuses.GRANTED,
    )
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

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
