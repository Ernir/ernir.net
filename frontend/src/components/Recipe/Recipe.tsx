import React from "react";
import "./Recipe.css";
import { useParams, useRouteMatch } from "react-router";
import { Link } from "react-router-dom";
import gql from "graphql-tag";
import { useQuery } from "@apollo/react-hooks";
import { LoadingSpinner } from "../LoadingSpinner/LoadingSpinner";
import ReactMarkdown from "react-markdown";
import { Helmet } from "react-helmet";

const GET_GALLERY = gql`
  query recipe($slug: String!) {
    recipe(slug: $slug) {
      id
      name
      description
      ingredients {
        id
        amount
        name
        unit {
          name
        }
      }
      instructionText
    }
  }
`;

export const Recipe: React.FC = () => {
  let { path, url } = useRouteMatch();
  let { slug } = useParams();
  const { loading, error, data } = useQuery(GET_GALLERY, {
    variables: { slug: slug },
  });
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
    <article>
      <Helmet>
        <title>
          Ernir.net {">"} recipes {">"} {data.recipe.name}
        </title>
        <meta name="description" content={data.recipe.description} />
      </Helmet>
      <h2 id={data.recipe.id}>
        <Link to={"/recipes"}>Recipes</Link> {"> "}
        <Link to={url}>{data.recipe.name}</Link>
      </h2>
      <section>
        <p>{data.recipe.description}</p>
        <h2>Hráefni</h2>
        <dl>
          {data.recipe.ingredients.map(
            (ingredient: {
              id: number;
              name: string;
              amount: number;
              unit: { name: string };
            }) => {
              return (
                <dt key={ingredient.id}>
                  {ingredient.amount} {ingredient.unit.name} {ingredient.name}
                </dt>
              );
            }
          )}
        </dl>
      </section>
      <section>
        <ReactMarkdown source={data.recipe.instructionText} />
      </section>
    </article>
  );
};
