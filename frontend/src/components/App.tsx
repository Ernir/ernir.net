import React from "react";
import "./App.css";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import Gallery from "react-photo-gallery";
import { photos } from "../photos";

class App extends React.Component {
  render() {
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
              </div>
            </Route>
            <Route path="/photos">
              <Gallery photos={photos} />
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
