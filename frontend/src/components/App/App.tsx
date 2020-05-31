import React from "react";
import "./App.css";
import { Switch, Route } from "react-router-dom";

import { PersonalGalleryList } from "../PersonalGalleryList/PersonalGalleryList";

const App: React.FC = () => {
  return (
    <div className="container">
      <Switch>
        <Route exact path="/">
          <div className="home">
            <h2>Home</h2>
          </div>
        </Route>
        <Route path="/photos">
          <PersonalGalleryList />
        </Route>
      </Switch>
    </div>
  );
};

export default App;
