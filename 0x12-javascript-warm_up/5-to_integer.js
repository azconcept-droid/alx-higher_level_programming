#!/usr/bin/node
/**
 * script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 */

const args = process.argv;
let convInt;

if (args.length === 2) {
  console.log('Not a number');
} else {
  convInt = parseInt(args[2]);
  if (convInt) {
    console.log(`My number: ${convInt}`);
  } else {
    console.log('Not a number');
  }
}
