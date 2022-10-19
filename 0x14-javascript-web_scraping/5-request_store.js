#!/usr/bin/node
// This script writes a string to a file.
const args = process.argv;
const fs = require('fs');
const request = require('request');
const url = args[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const writeStream = fs.createWriteStream(args[3]);
    writeStream.write(body);
    writeStream.end();
  }
});
