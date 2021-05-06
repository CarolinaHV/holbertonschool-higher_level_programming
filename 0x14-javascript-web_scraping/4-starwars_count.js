#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    let info = JSON.parse(body);
    info = info.results;
    let i = 0;
    let count = 0;
    while (info[i]) {
      for (let j = 0; info[i].characters[j]; j++) {
        if (info[i].characters[j].indexOf('/18') > -1) {
          count++;
        }
      }
      i++;
    }
    console.log(count);
  }
});
