#!/usr/bin/node
/**
 * Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
 * You must use the class notation for defining your class and extends
 * The constructor must take 1 argument: size
 * The constructor of Rectangle must be called (by using super())
 */

// const Rectangle = require('./4-rectangle');
class Square extends require('./5-square') {
  constructor (size) { super(size, size); }
  charPrint (c) {
    if (c === undefined) { this.print(); } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
