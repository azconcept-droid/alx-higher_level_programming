#!/usr/bin/node

/**
 * This script  imports an array and
 * computes a new array.Using a map.
 * A new list must be created with
 * each value equal to the value of the initial list
 * multiplied by the index in the list
 */
const list = require('./100-data').list;
const newList = list.map((element, index) => (element * index));
console.log(list);
console.log(newList);
