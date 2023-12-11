#!/usr/bin/node

if (process.argv.length < 4 || process.argv[3] === 1) {
  console.log(0);
} else {
  const num = [];
  for (let i = 2; i < process.argv.length; i++) {
    num.push(parseInt(process.argv[i]));
  }
  num.sort();
  num.reverse();
  console.log(num[1]);
}
