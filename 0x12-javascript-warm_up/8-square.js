#!/usr/bin/node
/*
  This script prints a square of length x
  Where x is the first argument of the script
*/

const inputArgs = process.argv;

const squareSize = parseInt(inputArgs[2])

if (squareSize) {
    for (let row = 0; row < squareSize; row++) {
      let printX = '';
      for (let col = 0; col < squareSize; col++) {
        printX += 'X';
      }
      console.log(printX);
    }
} else {
    console.log('Missing size');
}
