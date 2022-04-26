import React from "react";
import gql from "graphql-tag";
import { useQuery } from "@apollo/react-hooks";
import { LoadingSpinner } from "../LoadingSpinner/LoadingSpinner";
import { Helmet } from "react-helmet";
import {
  GoogleMap,
  HeatmapLayer,
  useJsApiLoader,
} from "@react-google-maps/api";

const GET_RESTAURANTS = gql`
  query {
    restaurants {
      id
      name
      locationLng
      locationLat
      heatmapWeight
    }
  }
`;

const containerStyle = {
  width: "100%",
  height: "1200px",
};

const center = {
  lat: 52.32587853655816,
  lng: 4.882333537153177,
};

export const RestaurantMap: React.FC = () => {
  const { loading, error, data } = useQuery(GET_RESTAURANTS);
  const { isLoaded, loadError } = useJsApiLoader({
    googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY || "",
    libraries: ["visualization"],
  });
  if (loading) {
    return (
      <div className="heatmap">
        <LoadingSpinner />
      </div>
    );
  }
  const renderMap = () => {
    return (
      <div className="heatmap">
        <Helmet>
          <title>
            Ernir.net {">"} projects {">"} heatmap
          </title>
          <meta name="description" content={"Restaurant heatmap"} />
        </Helmet>
        <GoogleMap mapContainerStyle={containerStyle} center={center} zoom={15}>
          <HeatmapLayer
            data={data.restaurants.map(
              (restaurant: { locationLat: number; locationLng: number }) =>
                new google.maps.LatLng(
                  restaurant.locationLat,
                  restaurant.locationLng
                )
            )}
          />
        </GoogleMap>
        <dl>
          {data.restaurants.map((restaurant: { id: number; name: string }) => {
            return <dt key={restaurant.id}>{restaurant.name}</dt>;
          })}
        </dl>
      </div>
    );
  };
  if (error) {
    return <div>Error! ${error.message}</div>;
  } else if (loadError) {
    return <div>Error! ${loadError.message}</div>;
  }
  return isLoaded ? (
    renderMap()
  ) : (
    <div className="heatmap">
      <LoadingSpinner />
    </div>
  );
};
