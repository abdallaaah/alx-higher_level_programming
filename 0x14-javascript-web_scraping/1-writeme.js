#!/usr/bin/node
// how to write file in node js
const fs = require('node:fs');
fs.writeFile(process.argv[2], process.argv[3], err => {
  if (err) {
    console.error(err);
  }
});
