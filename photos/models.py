from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Gallery(models.Model):
    """
    Represents a collection of Photos.
    """

    name = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Galleries"


class Photo(models.Model):
    """
    Represents a single photo in a gallery, along with meta information.
    """

    # The binary image file to be shown.
    image = models.ImageField(width_field="width", height_field="height")
    # Fields of the image, stored as part of the model for more efficient access.
    width = models.IntegerField()
    height = models.IntegerField()
    url = models.URLField(null=True, max_length=1024)
    # A human-readable description of the photo.
    description = models.TextField()
    # The single gallery this photo belongs to.
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ("image",)


@receiver(post_save, sender=Photo)
def update_photo_url(sender, instance: Photo, **kwargs):
    """
    Makes the URL of a photo available on the model object itself, so it won't require remote access.
    Done post-save so the provided URL is final.
    """
    if instance.url is None:
        instance.url = instance.image.url
        instance.save()
