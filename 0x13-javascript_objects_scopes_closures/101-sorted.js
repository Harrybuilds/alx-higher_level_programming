#!/usr/bin/node

/* const dict = require('./101-data').dict; */

const { dict } = require('./101-data');

const occurrencesDict = {};

// Iterate over the keys and values of the original dictionary
for (const [userId, occurrences] of Object.entries(dict)) {
  // If the occurrences count is not already a key in the new dictionary, initialize it as an empty array
  if (!occurrencesDict[occurrences]) {
    occurrencesDict[occurrences] = [];
  }
  // Push the user id to the list corresponding to its occurrences count
  occurrencesDict[occurrences].push(userId);
}

console.log(occurrencesDict);
