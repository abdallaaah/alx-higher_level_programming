#!/usr/bin/node

const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    for (let x = 0; x < this.height; x++) {
      let z = '';
      for (let y = 0; y < this.width; y++) {
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
