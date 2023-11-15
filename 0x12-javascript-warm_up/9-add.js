#!/usr/bin/node

function add (a, b) {
  return a + b;
}
const x = parseInt(process.argv[2], 10);
const y = parseInt(process.argv[3], 10);
const q = add(x, y);
console.log(q);
