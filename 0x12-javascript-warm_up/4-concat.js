#!/usr/bin/node
/* This script prints two arguments passed to it, in the following format: “ is ” */
const myVar = process.argv.slice(2);
if (myVar === 0) {
  console.log(undefined + ' is ' + undefined);
} else if (myVar === 1) {
  console.log(`${myVar}` + ' is ' + undefined);
} else {
  console.log(`${myVar[0]}` + ' is ' + `${myVar[1]}`);
}
