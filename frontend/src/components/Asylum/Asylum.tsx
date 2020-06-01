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
}

class ImageGroup {
  readonly svg: any;
  readonly members: PeopleGroup;

  constructor(svg: any, members: PeopleGroup) {
    this.svg = svg;
    this.members = members;
  }
}

const groups: ImageGroup[] = [
  new ImageGroup(<Couple />, new PeopleGroup(1, 1, 0, 0)),
  new ImageGroup(<CoupleChild />, new PeopleGroup(1, 1, 1, 0)),
  new ImageGroup(<CoupleChildren />, new PeopleGroup(1, 1, 1, 1)),
  new ImageGroup(<Man />, new PeopleGroup(1, 0, 0, 0)),
  new ImageGroup(<ManChild />, new PeopleGroup(1, 0, 1, 0)),
  new ImageGroup(<Woman />, new PeopleGroup(0, 1, 0, 0)),
  new ImageGroup(<WomanChild />, new PeopleGroup(0, 1, 0, 1)),
  new ImageGroup(<WomanChildren />, new PeopleGroup(0, 1, 1, 1)),
];

/*
 * From https://stackoverflow.com/a/6274381/1675015
 */
function shuffle(a: any[]) {
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

const people: { notGranted: PeopleGroup; granted: PeopleGroup } = {
  granted: new PeopleGroup(164, 107, 55, 50),
  notGranted: new PeopleGroup(568 - 164, 255 - 107, 159 - 55, 141 - 50),
};

function randomGroup(): ImageGroup {
  return groups[Math.floor(Math.random() * groups.length)];
}

function groupWithBoy(): ImageGroup {
  const withBoy: number[] = [1, 2, 4, 7];
  return groups[withBoy[Math.floor(Math.random() * withBoy.length)]];
}

function groupWithGirl(): ImageGroup {
  const withGirl: number[] = [2, 6, 7];
  return groups[withGirl[Math.floor(Math.random() * withGirl.length)]];
}

function renderPeople(stats: PeopleGroup): any[] {
  function addGroup(group: ImageGroup) {
    const withoutPicked = updated.subtract(group.members);
    if (withoutPicked.isValid()) {
      peopleComponents.push(group.svg);
      updated = withoutPicked;
    }
  }

  let peopleComponents: any[] = [];
  let updated = new PeopleGroup(
    stats.men,
    stats.women,
    stats.boys,
    stats.girls
  );

  while (updated.hasGirls()) {
    addGroup(groupWithGirl());
  }
  while (updated.hasBoys()) {
    addGroup(groupWithBoy());
  }
  while (updated.hasPeople()) {
    addGroup(randomGroup());
  }
  return shuffle(peopleComponents);
}

export const Asylum: React.FC = () => {
  return (
    <div className={"asylum"}>
      <h2>Not Granted</h2>
      <p>
        Asylum denied, Dublin regulation deportation, asylum granted elsewhere,
        other
      </p>
      {renderPeople(people.notGranted)}
      <h2>Granted</h2>
      <p>Granted, granted for humanitarian reasons</p>
      {renderPeople(people.granted)}
    </div>
  );
};
