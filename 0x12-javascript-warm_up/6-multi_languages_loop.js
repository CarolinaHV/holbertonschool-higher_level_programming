#!/usr/bin/node
/*
  This script prints 3 lines,
  but by using an array of string and a loop
*/
const languages = { C: 'fun', Python: 'cool', JavaScript: 'amazing' };

for (const value in languages) {
  console.log(`${value} is ${languages[value]}`);
}
