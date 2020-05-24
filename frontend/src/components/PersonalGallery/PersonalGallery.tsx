import React from "react";
import Gallery from "react-photo-gallery";

export interface PersonalGalleryProps {
  name: string;
  photoSet: { url: string; width: number; height: number }[];
}

export const PersonalGallery: React.FC<PersonalGalleryProps> = ({
  name,
  photoSet,
}) => {
  const photos = photoSet.map((photo) => ({
    src: photo.url,
    width: photo.width,
    height: photo.height,
  }));
  return (
    <div>
      <h2>{name}</h2>
      <Gallery photos={photos} />
    </div>
  );
};
