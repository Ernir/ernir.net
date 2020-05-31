import React from "react";
import Gallery from "react-photo-gallery";
import "./PersonalGallery.css";
import { useParams, useRouteMatch } from "react-router";
import { Link } from "react-router-dom";
import gql from "graphql-tag";
import { useQuery } from "@apollo/react-hooks";

const GET_GALLERY = gql`
  query gallery($identifier: String!) {
    gallery(identifier: $identifier) {
      name
      photoSet {
        width
        height
        url
      }
    }
  }
`;

export const PersonalGallery: React.FC = () => {
  let { path, url } = useRouteMatch();
  let { identifier } = useParams();
  const { loading, error, data } = useQuery(GET_GALLERY, {
    variables: { identifier: identifier },
  });
  if (loading) return <div>"Loading..."</div>;
  if (error) {
    return <div>Error! ${error.message}</div>;
  }
  const photos = data.gallery.photoSet.map(
    (photo: { url: string; width: number; height: number }) => {
      return {
        src: photo.url,
        width: photo.width,
        height: photo.height,
      };
    }
  );
  return (
    <div className="personal-gallery">
      <h2 id={identifier}>
        <Link to={"/photos"}>Photos</Link> >{" "}
        <Link to={url}>{data.gallery.name}</Link>
      </h2>
      <Gallery photos={photos} />
    </div>
  );
};
