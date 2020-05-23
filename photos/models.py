from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField()
    description = models.TextField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
