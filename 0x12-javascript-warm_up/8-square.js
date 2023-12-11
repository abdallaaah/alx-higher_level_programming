#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const n = parseInt(process.argv[2]);
  for (let x = 0; x < n; x++) {
    let row = ' ';
    for (let y = 0; y < n; y++) {
      row += ('X');
    }
    console.log(row);
  }
}
