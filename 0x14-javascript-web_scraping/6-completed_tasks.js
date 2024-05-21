#!/usr/bin/node
/*
  This script computes the number of tasks completed by user id.
*/
const args = process.argv;
const request = require('request');
const url = args[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const tasksCompleted = {};
    for (let i = 0; i <= 10; i++) {
      for (const user of JSON.parse(body)) {
        if (user.userId === i) {
          if (user.completed === true) {
            count++;
          }
        }
      }
      if (count !== 0) {
        tasksCompleted[i] = count;
      }
      count = 0;
    }

    console.log(tasksCompleted);
  }
});
