#!/usr/bin/node

if (process.argv.lenght < 2) {
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
