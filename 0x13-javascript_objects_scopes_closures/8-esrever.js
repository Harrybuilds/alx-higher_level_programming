#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];

  for (let i = list.legth - 1; i => 0; i--) {
    newlist.push(list[i]);
  }
  return newlist;
};
