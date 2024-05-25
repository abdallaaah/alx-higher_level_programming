#!/usr/bin/node
// count user completed task
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const object = JSON.parse(body);
  let count = 0;
  let userid = 0;
  const dict = {};
  for (let y = 0; y < object.length; y++) {
    userid = object[y]['userId']
  }
  for (let x = 1; x <= userid; x++) {
    count = 0;
    for (let y = 0; y < object.length; y++) {
      if (object[y].userId === x && object[y]['completed']) {
        count++;
      }
    }
    if (count != 0){
      dict[x] = count;
    }
    
  }
  if (dict != {}){
  console.log(dict);
  }
});
