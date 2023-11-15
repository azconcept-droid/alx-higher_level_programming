#!/usr/bin/node
/*
  This script prints 3 lines: (like 1-multi_languages.js) but
  by using an array of string and a loop
*/

const sweetSentences = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let i = 0;

while (sweetSentences[i]) {
  console.log(sweetSentences[i]);
  i++;
}
