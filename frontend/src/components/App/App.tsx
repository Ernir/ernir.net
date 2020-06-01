import React from "react";
import "./App.css";
import { Switch, Route, Link } from "react-router-dom";

import { PersonalGalleryList } from "../PersonalGalleryList/PersonalGalleryList";
import { PersonalGallery } from "../PersonalGallery/PersonalGallery";
import { Home } from "../Home/Home";

const App: React.FC = () => {
  return (
    <div className="container">
      <nav>
        <dl>
          <dt>
            <Link to="/">Home</Link>
          </dt>
          <dt>
            <Link to="/photos">Photos</Link>
          </dt>
        </dl>
      </nav>
      <hr />
      <Switch>
        <Route exact path="/">
          <div className="home">
            <Home />
          </div>
        </Route>
        <Route path="/photos/:identifier" children={<PersonalGallery />} />
        <Route path="/photos">
          <PersonalGalleryList />
        </Route>
      </Switch>
    </div>
  );
};

export default App;
