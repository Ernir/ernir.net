import React from "react";
import gql from "graphql-tag";
import { useQuery } from "@apollo/react-hooks";
import { LoadingSpinner } from "../LoadingSpinner/LoadingSpinner";
import { Helmet } from "react-helmet";

const GET_RESTAURANTS = gql`
  query {
    restaurants {
      id
      name
    }
  }
`;

export const RestaurantMap: React.FC = () => {
  const { loading, error, data } = useQuery(GET_RESTAURANTS);
  if (loading) {
    return (
      <div className="heatmap">
        <LoadingSpinner />
      </div>
    );
  }
  if (error) {
    return <div>Error! ${error.message}</div>;
  }
  return (
    <div className="heatmap">
      <Helmet>
        <title>
          Ernir.net {">"} projects {">"} heatmap
        </title>
        <meta name="description" content={"Restaurant heatmap"} />
      </Helmet>
      <dl>
        {data.restaurants.map((restaurant: { id: number; name: string }) => {
          return <dt key={restaurant.id}>{restaurant.name}</dt>;
        })}
      </dl>
    </div>
  );
};
