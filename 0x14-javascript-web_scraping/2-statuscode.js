#!/usr/bin/node
// this is to retrive status code form response in nodejs
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  console.log('code: %s', response.statusCode);
});
