#!/usr/bin/node
// This script reads and prints the content of a file.
const args = process.argv;
const fs = require('fs');

function readData (err, data) {
  console.log(data);
  if (err) {
    console.log(err);
  }
}

fs.readFile(args[2], 'utf8', readData);
