import React from "react";
import { useQuery } from "@apollo/react-hooks";
import gql from "graphql-tag";
import "./PersonalGalleryList.css";
import {
  PersonalGallery,
  PersonalGalleryProps,
} from "../PersonalGallery/PersonalGallery";

const GET_GALLERIES = gql`
  query {
    allGalleries {
      name
      identifier
      photoSet {
        url
        width
        height
      }
    }
  }
`;

export const PersonalGalleryList: React.FC = () => {
  const { loading, error, data } = useQuery(GET_GALLERIES);

  if (loading) return <div>"Loading..."</div>;
  if (error) {
    return <div>Error! ${error.message}</div>;
  }
  return data.allGalleries.map((gallery: PersonalGalleryProps) => {
    return (
      <div className="personal-galleries">
        <PersonalGallery
          identifier={gallery.identifier}
          name={gallery.name}
          photoSet={gallery.photoSet}
        />
      </div>
    );
  });
};
