#!/usr/bin/node

let a = 0;
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (a = 0; a < x; a++) {
    let line = '';
    for (let b = 0; b < x; b++) {
      line += 'x';
    }
    console.log(line);
  }
}
