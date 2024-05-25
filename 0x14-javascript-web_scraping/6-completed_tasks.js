#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  try {
    const tasks = JSON.parse(body);
    const userTaskCount = {};

    tasks.forEach(task => {
      if (task.completed) {
        if (!userTaskCount[task.userId]) {
          userTaskCount[task.userId] = 0;
        }
        userTaskCount[task.userId]++;
      }
    });

    console.log(userTaskCount);
  } catch (err) {
    console.log('Error parsing JSON:', err);
  }
});
