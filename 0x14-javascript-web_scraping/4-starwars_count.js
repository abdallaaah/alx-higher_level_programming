#!/usr/bin/node
let WedgeAntillesUrl = '';
const request = require('request');
const request2 = require('request');
const url = process.argv[2];

function MakeAnotherReq (url) {
  request2(url, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    const x = JSON.parse(body).films.length;
    console.log(x);
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const dict = JSON.parse(body);
  const character = dict.results[0].characters;
  for (let i = 0; i < character.length; i++) {
    const parts = character[i].split('/');
    if (parts[5] === '18') {
      WedgeAntillesUrl = (character[i]);
    }
  }
  MakeAnotherReq(WedgeAntillesUrl);
});
// request(wedge_antilles_url, (error, response, body) => {
//  if (error) {
//     console.log(error)
// }
// console.log(body)

// })
