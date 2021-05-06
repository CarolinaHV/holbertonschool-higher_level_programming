#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const emp = {};
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const info = JSON.parse(body);
    let i = 0;
    while (info[i]) {
      const userId = info[i].userId;
      let count = 0;
      let j = i;

      while (info[j] && info[j].userId === userId) {
        if (info[j].completed) {
          count++;
        }
        j++;
      }
      if (count != 0) {
      emp[userId] = count;
      }
      i = j;
    }
    console.log(emp);
  }
});
