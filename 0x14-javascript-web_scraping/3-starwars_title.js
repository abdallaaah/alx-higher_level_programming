#!/usr/bin/node
// this how to parse data body
const id = process.argv[2];
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${id}`, function(error, response, body) {
    if (error) {
    console.log(error);
    return;
    }
    const filmdata = JSON.parse(body);
    console.log(filmdata.title);
});