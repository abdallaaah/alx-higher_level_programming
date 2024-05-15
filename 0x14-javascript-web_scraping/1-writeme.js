#!/usr/bin/node
// this is how to write on file

const fs = require('fs');
const text = process.argv[3];
fs.writeFile(process.argv[2], text, (errr) => {
  if (errr) {
    console.log('aaaaaaaaa');
  }
});
