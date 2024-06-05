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
    } else if (res.statusCode === 200) {
      for (let k = 0; k < body.length; k++) {
        const task = body[k];
        if (task.completed) {
          if (taskCount[task.userId]) {
            taskCount[task.userId] += 1;
          } else {
            taskCount[task.userId] = 1;
          }
        }
      }
      console.log(taskCount);
    }
  });
};

numTask(process.argv[2]);
