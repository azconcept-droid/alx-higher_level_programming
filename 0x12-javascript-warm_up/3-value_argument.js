#!/usr/bin/node
// This script prints the first argument passed to it

const args = process.argv;

let count = 0;
while (args[count]) {
  count++; // count the number of arguments
}

if (count === 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
