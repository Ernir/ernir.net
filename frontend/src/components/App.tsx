import React from "react";
import "./App.css";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import Gallery from "react-photo-gallery";
import { photos } from "../photos";

import { useQuery } from "@apollo/react-hooks";
import gql from "graphql-tag";

const GET_GALLERIES = gql`
  query {
    allGalleries {
      name
      photoSet {
        url
      }
    }
  }
`;

const App: React.FC = () => {
  const { loading, error, data } = useQuery(GET_GALLERIES);

  if (loading) return <div>"Loading..."</div>;
  if (error) {
    return <div>Error! ${error.message}</div>;
  }
  return (
    <Router>
      <div>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/photos">Photos</Link>
          </li>
        </ul>
        <hr />
        <Switch>
          <Route exact path="/">
            <div className="home">
              <h2>Home</h2>
              <p>{data.allGalleries[0].name}</p>
            </div>
          </Route>
          <Route path="/photos">
            <Gallery photos={photos} />
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

export default App;
