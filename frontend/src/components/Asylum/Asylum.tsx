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

const numGranted = 376;
const numDenied = 747;

function nullArray(length: number): void[] {
  return Array.apply(null, Array(length)).map(function () {});
}

function people(number: number) {
  return nullArray(number).map((x: void) => (
    <span className={"person"}>
      <Man />
    </span>
  ));
}

export const Asylum: React.FC = () => {
  return (
    <div className={"asylum"}>
      <h2>Not Granted</h2>
      <p>Asylum denied, Dublin regulation deportation, asylum granted elsewhere, other</p>
      {people(numDenied)}
      <h2>Granted</h2>
      <p>Granted, granted for humanitarian reasons</p>
      {people(numGranted)}
    </div>
  );
};
