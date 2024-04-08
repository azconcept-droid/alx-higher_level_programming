#!/usr/bin/node
/*
  This script searches the second biggest
  integer in the list of arguments
*/

const argsList = process.argv;

if (argsList.length === 2 || argsList.length === 3) {
  console.log(0);
} else {
  // Slice out 1st two elements
  const numList = argsList.slice(2);
  // Sort in descending order
  const sortedNumbers = numList.sort((a, b) => b - a);

  console.log(sortedNumbers[1]);
}
