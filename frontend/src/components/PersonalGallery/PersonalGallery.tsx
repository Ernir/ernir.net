import React from "react";
import Gallery from "react-photo-gallery";

export interface PersonalGalleryProps {
  identifier: string;
  name: string;
  photoSet: { url: string; width: number; height: number }[];
}

export const PersonalGallery: React.FC<PersonalGalleryProps> = ({
  identifier,
  name,
  photoSet,
}) => {
  const photos = photoSet.map((photo) => ({
    src: photo.url,
    width: photo.width,
    height: photo.height,
  }));
  return (
    <div className="personal-gallery">
      <h2 id={identifier}>{name}</h2>
      <Gallery photos={photos} />
    </div>
  );
};
