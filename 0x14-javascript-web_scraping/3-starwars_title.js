#!/usr/bin/node

const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episode;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const info = JSON.parse(body);
    console.log(info.title);
  }
});
