#!/usr/bin/node
/*
  This script prints x times “C is fun”
  Where x is the first argument of the script
*/

const inputArgs = process.argv;

const x = parseInt(inputArgs[2]);

if (inputArgs.length === 2) { console.log('Missing number of occurrences'); }

if (x) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
  
