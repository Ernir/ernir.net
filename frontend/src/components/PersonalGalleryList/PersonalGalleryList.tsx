import React from "react";
import "./PersonalGalleryList.css";
import { useQuery } from "@apollo/react-hooks";
import gql from "graphql-tag";
import { useRouteMatch } from "react-router";
import { Link } from "react-router-dom";
import { LoadingSpinner } from "../LoadingSpinner/LoadingSpinner";

const GET_GALLERIES = gql`
  query {
    allGalleries {
      name
      identifier
    }
  }
`;

export const PersonalGalleryList: React.FC = () => {
  const { loading, error, data } = useQuery(GET_GALLERIES);
  let { path } = useRouteMatch();

  if (loading) {
    return (
      <div className="personal-galleries">
        <h2>
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
    <div className="personal-galleries">
      <h2>
        <Link to={"/photos"}>Photos</Link>{" "}
      </h2>
      <dl>
        {data.allGalleries.map(
          (gallery: { identifier: string; name: string }) => {
            return (
              <dt key={gallery.identifier}>
                <Link to={`${path}/${gallery.identifier}`}>{gallery.name}</Link>
              </dt>
            );
          }
        )}
      </dl>
    </div>
  );
};
