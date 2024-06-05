#!/usr/bin/node

const request = require('request');

const starWarsCount = (api) => {
  const apiObject = {
    uri: api,
    method: 'GET',
    json: true
  };
  const xter = 'https://swapi-api.alx-tools.com/api/people/18/';
  request(apiObject, (err, res, body) => {
    if (err) {
      console.error(err);
    }
    let count = 0;
    for (let i = 0; i < body.results.length; i++) {
      if (body.results[i].characters.includes(xter)) { count += 1; }
    }

    console.log(count);
  });
};

starWarsCount(process.argv[2]);
