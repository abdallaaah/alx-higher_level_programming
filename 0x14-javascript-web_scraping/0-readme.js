#!/usr/bin/node

const fs = require('fs');

fs.readFile('my_file.txt', 'utf-8', function (errr, data) {
  if (errr) {
    console.log(errr);
    return;
  }
  console.log(data);
});
