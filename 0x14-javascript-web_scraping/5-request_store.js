#!/usr/bin/node

const request = require('request');
const fs = require('node:fs');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
