#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}
if (parseInt(process.argv[2]) && parseInt(process.argv[3])) {
  add(parseInt(process.argv[2]), parseInt(process.argv[3]));
} else {
  console.log('NaN');
}
