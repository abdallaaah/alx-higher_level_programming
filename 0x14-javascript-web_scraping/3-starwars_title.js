#!/usr/bin/node
// fetch movie name

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (error, response, body) => {
  if (error) {
    console.log(url);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
