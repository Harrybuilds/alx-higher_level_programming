#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let c = 0;

  while (c < x) {
    theFunction();
    c++;
  }
};
