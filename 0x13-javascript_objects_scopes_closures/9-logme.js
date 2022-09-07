#!/usr/bin/node

/**
 * This script prints the number of arguments
 * already printed and the new argument value
 */
let functionCall = 0;
exports.logMe = function (item) {
  console.log(`${functionCall++}: ${item}`);
};
