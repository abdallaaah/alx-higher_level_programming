#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || h <= 0 || !w || !h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let z = '';
      for (let y = 0; y < this.width; y++) {
        z += ('X');
      }
      console.log(z);
    }
  }
}
module.exports = Rectangle;
