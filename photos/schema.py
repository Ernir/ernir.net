import graphene

from graphene_django.types import DjangoObjectType

from photos.models import Gallery, Photo


class GalleryType(DjangoObjectType):
    class Meta:
        model = Gallery


class PhotoType(DjangoObjectType):

    src = graphene.String()

    def resolve_src(self, info, **kwargs):
        return self.image.url

    class Meta:
        model = Photo


class Query(object):
    gallery = graphene.Field(GalleryType, identifier=graphene.String())
    all_galleries = graphene.List(GalleryType)
    all_photos = graphene.List(PhotoType)

    def resolve_gallery(self, info, **kwargs):
        identifier = kwargs.get("identifier")
        return Gallery.objects.get(identifier=identifier)

    def resolve_all_galleries(self, info, **kwargs):
        return Gallery.objects.all()

    def resolve_all_photos(self, info, **kwargs):
        return Photo.objects.select_related("gallery").all()
