#!/usr/bin/node
// this is how to count char movies with web scraping

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const filmdata = JSON.parse(body).results;
  let number = 0;
  for (let i = 0; i < filmdata.length; i++) {
    const charctersList = filmdata[i].characters;
    for (let x = 0; x < charctersList.length; x++) {
      const id = charctersList[x].split('/')[5];
      if (id === '18') {
        number++;
      }
    }
  }
  console.log(number);
}
);
