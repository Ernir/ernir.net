import React from "react";
import "./Home.css";
import { useQuery } from "@apollo/react-hooks";
import gql from "graphql-tag";
import ReactMarkdown from "react-markdown";
import { Asylum } from "../Asylum/Asylum";

const GET_HOME = gql`
  query {
    allFrontpageSections {
      mainText
    }
  }
`;

export const Home: React.FC = () => {
  const { loading, error, data } = useQuery(GET_HOME);
  if (loading) return <div>"Loading..."</div>;
  if (error) {
    return <div>Error! ${error.message}</div>;
  }
  return (
    <div className={"home"}>
      {data.allFrontpageSections.map((section: { mainText: string }) => (
        <ReactMarkdown source={section.mainText} />
      ))}
      <Asylum />
    </div>
  );
};
