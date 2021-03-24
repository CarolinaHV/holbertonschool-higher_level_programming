#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const data = list.map((number, i) => { return number * i; });
console.log(data);
