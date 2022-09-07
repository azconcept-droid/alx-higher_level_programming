#!/usr/bin/node
/**
 * This script create a class Rectangle
 * that defines a rectangle.
 * If w or h is equal to 0 or not a positive integer,
 * create an empty object.
 * Create an instance method called print()
 * that prints the rectangle using the character X
 * Create an instance method called rotate()
 * that exchanges the width and the height of the rectangle
 * Create an instance method called double()
 * that multiples the width and the height of the rectangle by 2
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rectRow = ''; // hold X to display horizontally
      for (let j = 0; j < this.width; j++) {
        rectRow += 'X'; // append horizontally at console
      }
      console.log(rectRow);
    }
  }

  rotate () {
    const holdForme = this.width;
    this.width = this.height;
    this.height = holdForme;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
