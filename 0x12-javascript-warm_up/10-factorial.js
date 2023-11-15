#!/usr/bin/node

function factorialize (num) {
  if (num === 0 || num === 1) { return 1; }
  for (let i = num - 1; i >= 1; i--) {
    num *= i;
  }
  return num;
}
if (process.argv[2] == null) {
  console.log(1);
} else {
  console.log(factorialize(process.argv[2]));
}
