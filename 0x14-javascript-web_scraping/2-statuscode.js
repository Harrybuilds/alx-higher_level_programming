#!/usr/bin/node
const request = require('request');

const checkStatusCode = (reqObject) => {
  request(reqObject, (err, res, body) => {
    if (err) {
      console.error(err);
    }
    console.log('code:', res.statusCode);
  });
};

const url = process.argv[2];

const urlObj = {
  method: 'GET',
  uri: url
};

checkStatusCode(urlObj);
