import React from "react";
import "./LoadingSpinner.css";

/**
 * Source: https://loading.io/css/
 */
export const LoadingSpinner: React.FC = () => {
  return (
    <div className="lds-ellipsis">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
  );
};
