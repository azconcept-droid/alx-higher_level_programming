#!/usr/bin/node
// This script writes a string to a file.
const args = process.argv;
const fs = require('fs');

const writeStream = fs.createWriteStream(args[2]);
writeStream.write(args[3]);
writeStream.end();
