import graphene

from graphene_django.types import DjangoObjectType

from photos.models import Gallery, Photo


class GalleryType(DjangoObjectType):
    class Meta:
        model = Gallery


class PhotoType(DjangoObjectType):
    url = graphene.String()
    width = graphene.Int()
    height = graphene.Int()

    def resolve_url(self, info):
        return self.image.url

    def resolve_width(self, info):
        return self.image.width

    def resolve_height(self, info):
        return self.image.height

    class Meta:
        model = Photo


class Query(object):
    all_galleries = graphene.List(GalleryType)
    all_photos = graphene.List(PhotoType)

    def resolve_all_galleries(self, info, **kwargs):
        return Gallery.objects.all()

    def resolve_all_photos(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Photo.objects.select_related("gallery").all()
