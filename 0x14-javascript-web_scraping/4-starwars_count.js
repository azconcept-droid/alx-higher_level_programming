#!/usr/bin/node
/*
  This script prints the number of movies
  where the character “Wedge Antilles” is present.
*/
const args = process.argv;
const request = require('request');
const url = args[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).results);
  }
});
