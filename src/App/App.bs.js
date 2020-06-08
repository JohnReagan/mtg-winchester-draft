'use strict';

var React = require("react");

function App(Props) {
  return React.createElement("div", undefined, "Hello Winchester Draft");
}

var make = App;

exports.make = make;
/* react Not a pure module */
