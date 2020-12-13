import React from "react";
import "./App.css";
import { Switch, Route, Link } from "react-router-dom";
import { Helmet } from "react-helmet";

import { PersonalGalleryList } from "../PersonalGalleryList/PersonalGalleryList";
import { PersonalGallery } from "../PersonalGallery/PersonalGallery";
import { TextPage } from "../TextPage/TextPage";
import { Asylum } from "../Asylum/Asylum";
import { RecipeList } from "../RecipeList/RecipeList";
import { Recipe } from "../Recipe/Recipe";

const App: React.FC = () => {
  return (
    <div className="container">
      <Helmet>
        <title>Ernir.net</title>
        <meta
          name="description"
          content="Eiríkur Ernir Þorsteinsson's personal homepage"
        />
      </Helmet>
      <nav>
        <dl>
          <dt>
            <Link to="/">Home</Link>
          </dt>
          <dt>
            <Link to="/photos">Photos</Link>
          </dt>
          <dt>
            <Link to="/projects">Projects</Link>
          </dt>
          <dt>
            <Link to="/recipes">Recipes</Link>
          </dt>
        </dl>
      </nav>
      <hr />
      <Switch>
        <Route exact path="/">
          <TextPage category={"FRONT_PAGE"} />
        </Route>
        <Route path="/projects/asylum">
          <Asylum />
        </Route>
        <Route path="/projects">
          <TextPage category={"PROJECTS"} />
        </Route>
        <Route path="/photos/:identifier" children={<PersonalGallery />} />
        <Route path="/photos">
          <PersonalGalleryList />
        </Route>
        <Route path="/recipes/:slug" children={<Recipe />} />
        <Route path="/recipes">
          <RecipeList />
        </Route>
      </Switch>
    </div>
  );
};

export default App;
