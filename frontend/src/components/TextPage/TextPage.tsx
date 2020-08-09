import React from "react";
import "./TextPage.css";
import { useQuery } from "@apollo/react-hooks";
import gql from "graphql-tag";
import ReactMarkdown from "react-markdown";

const GET_SECTIONS = gql`
  query sections($category: String!) {
    sections(category: $category) {
      mainText
    }
  }
`;

interface TextPageProps {
  category: string;
}

export const TextPage: React.FC<TextPageProps> = (props) => {
  const { loading, error, data } = useQuery(GET_SECTIONS, {
    variables: { category: props.category },
  });
  if (loading) {
    return <div>"Loading..."</div>;
  }
  if (error) {
    return <div>Error! ${error.message}</div>;
  }
  return (
    <div className={"text-page"}>
      {data.sections.map((section: { mainText: string }) => (
        <ReactMarkdown source={section.mainText} />
      ))}
    </div>
  );
};
