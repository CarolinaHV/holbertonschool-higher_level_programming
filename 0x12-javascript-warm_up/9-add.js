#!/usr/bin/node
/*
  This script that prints the addition of 2 integers
  The first argument is the first integer
  The second argument is the second integer
*/
function add (a, b) {
  return a + b;
}

const num = (process.argv.slice(2));

if (parseInt(num[0]) && parseInt(num[1])) {
  console.log(add(parseInt(`${num[0]}`), parseInt(`${num[1]}`)));
} else if (parseInt(num[0]) && num[1] === undefined) {
  console.log(NaN);
} else {
  console.log(NaN);
}
