import React from "react";
import "./App.css";
import { Switch, Route, Link, BrowserRouter as Router } from "react-router-dom";

import { PersonalGalleryList } from "../PersonalGalleryList/PersonalGalleryList";
import { PersonalGallery } from "../PersonalGallery/PersonalGallery";

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
            <h2>Home</h2>
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
