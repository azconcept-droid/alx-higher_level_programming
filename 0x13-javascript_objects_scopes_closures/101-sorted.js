#!/usr/bin/node

/**
 * Write a script that imports a dictionary of
 * occurrences by user id and computes a dictionary of user ids by occurrence.
 */
const { dict = {} } = require('./101-data.js');
const newDict = {};

for (const key in dict) {
  const value = dict[key];
  if (newDict[value]) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}

console.log(newDict);