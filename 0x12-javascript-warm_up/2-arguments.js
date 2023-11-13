#!/usr/bin/node
/**
 * This script prints a message
 * depending of the number of arguments passed
 */

const args = process.argv;

if (args.length === 2) {
  console.log('No argument');
} else {
  console.log(`${(args.length === 3) ? "Argument found" : "Arguments found"}`);
}
