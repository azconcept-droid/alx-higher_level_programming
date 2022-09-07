#!/usr/bin/node
/**
 * This script create a class Square
 * that inherits from Square.
 * Create an instance method called charPrint(c)
 * that prints the rectangle using the character c
 * If c is undefined, use the character X
 */
const parentSquare = require('./5-square');

class Square extends parentSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c == null) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let rectRow = ''; // hold custom c to display horizontally
        for (let j = 0; j < this.width; j++) {
          rectRow += c; // append horizontally at console
        }
        console.log(rectRow);
      }
    }
  }
}

module.exports = Square;
