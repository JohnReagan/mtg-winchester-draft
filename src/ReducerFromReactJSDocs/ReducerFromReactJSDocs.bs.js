'use strict';

var Curry = require("bs-platform/lib/js/curry.js");
var React = require("react");

var leftButtonStyle = {
  width: "48px",
  borderRadius: "4px 0px 0px 4px"
};

var rightButtonStyle = {
  width: "48px",
  borderRadius: "0px 4px 4px 0px"
};

var containerStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "space-between"
};

var initialState = {
  count: 0
};

function reducer(state, action) {
  if (action) {
    return {
            count: state.count - 1 | 0
          };
  } else {
    return {
            count: state.count + 1 | 0
          };
  }
}

function ReducerFromReactJSDocs(Props) {
  var match = React.useReducer(reducer, initialState);
  var dispatch = match[1];
  return React.createElement("div", {
              style: containerStyle
            }, React.createElement("div", undefined, "Count: ", String(match[0].count)), React.createElement("div", undefined, React.createElement("button", {
                      style: leftButtonStyle,
                      onClick: (function (_event) {
                          return Curry._1(dispatch, /* Decrement */1);
                        })
                    }, "-"), React.createElement("button", {
                      style: rightButtonStyle,
                      onClick: (function (_event) {
                          return Curry._1(dispatch, /* Increment */0);
                        })
                    }, "+")));
}

var make = ReducerFromReactJSDocs;

exports.leftButtonStyle = leftButtonStyle;
exports.rightButtonStyle = rightButtonStyle;
exports.containerStyle = containerStyle;
exports.initialState = initialState;
exports.reducer = reducer;
exports.make = make;
/* react Not a pure module */
