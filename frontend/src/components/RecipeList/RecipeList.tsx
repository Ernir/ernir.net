import React from "react";
import "./RecipeList.css";
import { useQuery } from "@apollo/react-hooks";
import gql from "graphql-tag";
import { useRouteMatch } from "react-router";
import { Link } from "react-router-dom";
import { LoadingSpinner } from "../LoadingSpinner/LoadingSpinner";
import { Helmet } from "react-helmet";

const GET_RECIPES = gql`
  query {
    recipes {
      id
      name
      description
      slug
    }
  }
`;

export const RecipeList: React.FC = () => {
  const { loading, error, data } = useQuery(GET_RECIPES);
  let { path } = useRouteMatch();

  if (loading) {
    return (
      <div>
        <h2>
          <Link to={"/recipes"}>Recipes</Link>
        </h2>
        <LoadingSpinner />
      </div>
    );
  }
  if (error) {
    return <div>Error! ${error.message}</div>;
  }
  return (
    <div className="recipes">
      <Helmet>
        <title>Ernir.net {">"} recipes</title>
        <meta name="description" content="Ernir & Hrefna's food recipes" />
      </Helmet>
      <h2>
        <Link to={"/recipes"}>Recipes</Link>{" "}
      </h2>
      <dl>
        {data.recipes.map(
          (recipe: {
            id: number;
            name: string;
            slug: string;
            description: string;
          }) => {
            return (
              <dt key={recipe.id}>
                <Link to={`${path}/${recipe.slug}`}>{recipe.name}</Link>{" "}
                {recipe.description}
              </dt>
            );
          }
        )}
      </dl>
    </div>
  );
};
