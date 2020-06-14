import React from "react";
import "./Asylum.css";
import { ReactComponent as Couple } from "./couple.svg";
import { ReactComponent as CoupleChild } from "./couple-child.svg";
import { ReactComponent as CoupleChildren } from "./couple-children.svg";
import { ReactComponent as Man } from "./man.svg";
import { ReactComponent as ManChild } from "./man-child.svg";
import { ReactComponent as Woman } from "./woman.svg";
import { ReactComponent as WomanChild } from "./woman-child.svg";
import { ReactComponent as WomanChildren } from "./woman-children.svg";
import { shuffle } from "../../utils";
import gql from "graphql-tag";
import { useQuery } from "@apollo/react-hooks";
import { LoadingSpinner } from "../LoadingSpinner/LoadingSpinner";

/**
 * A group consisting of the four types of people (I know, right?) recognized by the Icelandic Directorate of Immigration: men, women, boys and girls.
 */
class PeopleGroup {
  men: number;
  women: number;
  boys: number;
  girls: number;

  constructor(men: number, women: number, boys: number, girls: number) {
    this.men = men;
    this.women = women;
    this.boys = boys;
    this.girls = girls;
  }

  subtract(otherGroup: PeopleGroup): PeopleGroup {
    return new PeopleGroup(
      this.men - otherGroup.men,
      this.women - otherGroup.women,
      this.boys - otherGroup.boys,
      this.girls - otherGroup.girls
    );
  }

  isValid(): boolean {
    return (
      this.men >= 0 && this.women >= 0 && this.boys >= 0 && this.girls >= 0
    );
  }

  hasPeople(): boolean {
    return this.men > 0 || this.women > 0 || this.hasBoys() || this.hasGirls();
  }

  hasBoys(): boolean {
    return this.boys > 0;
  }

  hasGirls(): boolean {
    return this.girls > 0;
  }

  /**
   * Returns a randomized series of SVGs representing this group of people.
   */
  render(): any[] {
    function addGroup(group: ImageGroup) {
      const withoutPicked = updated.subtract(group.members);
      if (withoutPicked.isValid()) {
        peopleComponents.push(group.svg);
        updated = withoutPicked;
      }
    }

    let peopleComponents: any[] = [];
    let updated = new PeopleGroup(this.men, this.women, this.boys, this.girls);

    while (updated.hasGirls()) {
      addGroup(ImageGroup.groupWithGirl());
    }
    while (updated.hasBoys()) {
      addGroup(ImageGroup.groupWithBoy());
    }
    while (updated.hasPeople()) {
      addGroup(ImageGroup.randomGroup());
    }
    return shuffle(peopleComponents);
  }
}

/**
 * A relationship between a {@link PeopleGroup} and an SVG image.
 */
class ImageGroup {
  private static readonly knownGroupTypes: ImageGroup[] = [
    new ImageGroup(<Couple />, new PeopleGroup(1, 1, 0, 0)),
    new ImageGroup(<CoupleChild />, new PeopleGroup(1, 1, 1, 0)),
    new ImageGroup(<CoupleChildren />, new PeopleGroup(1, 1, 1, 1)),
    new ImageGroup(<Man />, new PeopleGroup(1, 0, 0, 0)),
    new ImageGroup(<ManChild />, new PeopleGroup(1, 0, 1, 0)),
    new ImageGroup(<Woman />, new PeopleGroup(0, 1, 0, 0)),
    new ImageGroup(<WomanChild />, new PeopleGroup(0, 1, 0, 1)),
    new ImageGroup(<WomanChildren />, new PeopleGroup(0, 1, 1, 1)),
  ];

  readonly svg: any;
  readonly members: PeopleGroup;

  constructor(svg: any, members: PeopleGroup) {
    this.svg = svg;
    this.members = members;
  }

  static randomGroup(): ImageGroup {
    return ImageGroup.knownGroupTypes[
      Math.floor(Math.random() * ImageGroup.knownGroupTypes.length)
    ];
  }

  static groupWithBoy(): ImageGroup {
    const withBoy: number[] = [1, 2, 4, 7];
    return ImageGroup.knownGroupTypes[
      withBoy[Math.floor(Math.random() * withBoy.length)]
    ];
  }

  static groupWithGirl(): ImageGroup {
    const withGirl: number[] = [2, 6, 7];
    return ImageGroup.knownGroupTypes[
      withGirl[Math.floor(Math.random() * withGirl.length)]
    ];
  }
}

const GET_PEOPLE = gql`
  query {
    totalGranted {
      men
      women
      boys
      girls
    }
    totalNotGranted {
      men
      women
      boys
      girls
    }
    updatedAt
  }
`;

export const Asylum: React.FC = () => {
  const { loading, error, data } = useQuery(GET_PEOPLE);
  if (loading) return <LoadingSpinner />;
  if (error) {
    return <div>Error! ${error.message}</div>;
  }
  const { totalGranted, totalNotGranted } = data;
  const people: { notGranted: PeopleGroup; granted: PeopleGroup } = {
    granted: new PeopleGroup(
      totalGranted.men,
      totalGranted.women,
      totalGranted.boys,
      totalGranted.girls
    ),
    notGranted: new PeopleGroup(
      totalNotGranted.men,
      totalNotGranted.women,
      totalNotGranted.boys,
      totalNotGranted.girls
    ),
  };
  return (
    <div className={"asylum"}>
      <h2>Not Granted</h2>
      <p>
        Asylum denied, Dublin regulation deportation, asylum granted elsewhere,
        other
      </p>
      {people.notGranted.render()}
      <h2>Granted</h2>
      <p>Granted, granted for humanitarian reasons</p>
      {people.granted.render()}
      <p>
        Latest update: {new Date(data.updatedAt).toLocaleDateString("is-IS")}.
      </p>
    </div>
  );
};
