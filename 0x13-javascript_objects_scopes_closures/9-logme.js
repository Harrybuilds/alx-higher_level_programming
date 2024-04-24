#!/usr/bin/node

exports.logMe = (function (item) {
  let count = 0;
  return function (newItem) {
    console.log(`${count}: ${newItem}`);
    count++;
  };
}());
