from django.db import models


class Gallery(models.Model):
    """
    Represents a collection of Photos.
    """

    name = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200, unique=True)
    start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-start_date", "identifier")
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
    # A human-readable description of the photo.
    description = models.TextField()
    # The single gallery this photo belongs to.
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ("image",)
