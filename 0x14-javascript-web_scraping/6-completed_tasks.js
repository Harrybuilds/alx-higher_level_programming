#!/usr/bin/node

const request = require('request');

const numTask = (url) => {
  const taskCount = {};

  const options = {
    uri: url,
    method: 'GET',
    json: true
  };

  request(options, (err, res, body) => {
    if (err) {
      console.error(err);
    }
    for (let k = 0; k < body.length; k++) {
      const task = body[k];
      if (task.completed) {
          if (task.userId in taskCount) {
              taskCount[task.userId]++;
          } else {
              taskCount[task.userId] = 1;
          }
      }
    }
    console.log(taskCount);
  });
};

numTask(process.argv[2]);