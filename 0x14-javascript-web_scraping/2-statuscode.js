#!/usr/bin/node
// This script displays the status code of a GET request.
const args = process.argv;
const request = require('request');
const url = args[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
