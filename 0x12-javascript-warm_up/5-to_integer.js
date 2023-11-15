#!/usr/bin/node

let x;
if (process.argv.length === 2) { 
console.log('Not a number');
} else {
x = parseInt(process.argv[2], 10);
if (!isNaN(x)) {
console.log(`My number: ${x}`)
} else {
console.log('Not a number');
}
}
