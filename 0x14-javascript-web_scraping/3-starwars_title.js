#!/usr/bin/node

const request = require('request');

const starWarsTitle = (id) => {
  const options = {
    uri: `https://swapi-api.alx-tools.com/api/films/${id}`,
    method: 'GET',
    json: true
  };
  request(options, (err, res, body) => {
    if (err) {
      console.error(err);
    }
    console.log(body.title);
  });
};

starWarsTitle(process.argv[2]);
