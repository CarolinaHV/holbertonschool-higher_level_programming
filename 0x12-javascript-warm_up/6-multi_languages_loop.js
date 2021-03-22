#!/usr/bin/node
/*
  This script prints 3 lines,
  but by using an array of string and a loop
*/
const objects = { C: 'fun', Python: 'cool', JavaScript: 'amazing' };

for (const value in objects) {
  console.log(`${value} is ${objects[value]}`);
}
