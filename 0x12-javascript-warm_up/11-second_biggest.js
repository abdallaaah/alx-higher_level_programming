#!/usr/bin/node

const len = process.argv.length;
if (len === 3) {
  console.log(0);
} else if (len === 2) {
  console.log(0);
} else if (parseInt(process.argv[3] == 1)) {
console.log(0);
}
else {
  let max = -999;
  let max2 = -9999;
  let num = 0;
  let num2 = 0;
  for (let i = 0; i < len; i++) {
    num = parseInt(process.argv[i], 10);
    if (max < num) {
      max = num;
    }
  }
  console.log('maxxx', max);
  for (let i = 0; i < len; i++) {
    num2 = parseInt(process.argv[i], 10);
    if (max2 < num2 && num2 !== max) {
      max2 = num2;
    }
  }
  console.log(max2);
}
