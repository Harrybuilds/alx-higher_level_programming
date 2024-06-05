#!/usr/bin/node
/***
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
*/



const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
