import React from "react";
import Gallery from "react-photo-gallery";
import "./PersonalGallery.css";
import { useParams, useRouteMatch } from "react-router";
import { Link } from "react-router-dom";
import gql from "graphql-tag";
import { useQuery } from "@apollo/react-hooks";
import { LoadingSpinner } from "../LoadingSpinner/LoadingSpinner";
import { Helmet } from "react-helmet";

const GET_GALLERY = gql`
  query gallery($identifier: String!) {
    gallery(identifier: $identifier) {
      name
      photoSet {
        width
        height
        src
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
  if (loading) {
    return (
      <div className="personal-gallery">
        <h2 id={identifier}>
          <Link to={"/photos"}>Photos</Link>
        </h2>
        <LoadingSpinner />
      </div>
    );
  }
  if (error) {
    return <div>Error! ${error.message}</div>;
  }
  return (
    <div className="personal-gallery">
      <Helmet>
        <title>
          Ernir.net {">"} photos {">"} {data.gallery.name}
        </title>
        <meta name="description" content={"Photos from " + data.gallery.name} />
      </Helmet>
      <h2 id={identifier}>
        <Link to={"/photos"}>Photos</Link> {"> "}
        <Link to={url}>{data.gallery.name}</Link>
      </h2>
      <Gallery photos={data.gallery.photoSet} />
    </div>
  );
};
