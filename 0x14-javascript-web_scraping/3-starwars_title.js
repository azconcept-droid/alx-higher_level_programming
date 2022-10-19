#!/usr/bin/node
/*
  This script prints the title of a Star Wars movie
  where the episode number matches a given integer.
*/
const args = process.argv;
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${args[2]}`;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
