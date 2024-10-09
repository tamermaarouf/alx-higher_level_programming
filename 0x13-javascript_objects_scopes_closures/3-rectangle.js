#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle:

// eslint-disable-next-line no-unused-vars, no-shadow
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let chr = '';
      for (let j = 0; j < this.width; j++) {
        chr += 'X';
      }
      console.log(chr);
    }
  }
}
module.exports = Rectangle;
