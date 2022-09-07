#!/usr/bin/node
/**
 * This script create a class Square
 * that inherits from Rectangle
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
