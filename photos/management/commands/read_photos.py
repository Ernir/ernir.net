import os
from typing import List

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from dropbox import dropbox
from dropbox.files import FolderMetadata, FileMetadata

from photos.models import Photo, Gallery


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.galleries_prefix = "/galleries"
        self.dbx = dropbox.Dropbox(os.environ.get("DROPBOX_OAUTH2_TOKEN"))

    def get_folders(self) -> List[str]:
        """
        :return the names of folders in this application's gallery Dropbox directory, see self.galleries_prefix.
        """
        for f in self.dbx.files_list_folder(self.galleries_prefix).entries:
            if isinstance(f, FolderMetadata):
                yield f.name

    def get_files_of_folder(self, folder_name) -> List[str]:
        """
        :param folder_name: the name of a Dropbox folder
        :return the names of files in the given Dropbox folder
        """
        path = f"{self.galleries_prefix}/{folder_name}"
        for f in self.dbx.files_list_folder(path).entries:
            if isinstance(f, FileMetadata):
                yield f.name

    def instantiate_from_folder(self, folder):
        gallery, created = Gallery.objects.get_or_create(identifier=folder)
        if created:
            gallery.name = gallery.identifier
            gallery.save()
        existing_photos = {photo.image for photo in gallery.photo_set.all()}
        files_on_dropbox = {
            f"{self.galleries_prefix}/{folder}/{filename}" for filename in self.get_files_of_folder(folder)
        }
        added = files_on_dropbox.difference(existing_photos)
        for path in added:
            print(f"Adding {path}")
            photo = Photo()
            photo.image = path
            photo.description = path
            photo.gallery = gallery
            photo.save()
        removed = existing_photos.difference(files_on_dropbox)
        for photo in gallery.photo_set.filter(image__in=removed).all():
            print(f"Removing {photo}")
            photo.delete()

    def handle(self, *args, **options) -> None:
        for folder in self.get_folders():
            self.instantiate_from_folder(folder)
