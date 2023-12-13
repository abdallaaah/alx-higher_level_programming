#!/usr/bin/node

const square = require('./5-square');
class Square extends square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let x = 0; x < this.size; x++) {
      let z = '';
      for (let y = 0; y < this.size; y++) {
        if (!c) {
          z += ('X');
        } else {
          z += (c);
        }
      }
      console.log(z);
    }
  }
}
module.exports = Square;
