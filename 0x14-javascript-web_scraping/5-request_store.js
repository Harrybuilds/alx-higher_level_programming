#!/usr/bin/node

const request = require('request');
const fs = require('fs').promises;

const getContents = (url, filepath) => {
  const options = {
    uri: url,
    method: 'GET'
  };

  request(options, (err, res, body) => {
    if (err) {
      console.error(err);
      return;
    }
    fs.writeFile(filepath, body, 'utf8', { mode: 'w' });
  });
};
const url = process.argv[2];
const filepath = process.argv[3];

getContents(url, filepath);
