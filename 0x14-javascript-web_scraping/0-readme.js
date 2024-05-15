#!/usr/bin/node
// snsfknskfnsf

const fs = require('fs');

fs.readFile('my_file.txt', 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
