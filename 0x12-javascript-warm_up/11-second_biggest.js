#!/usr/bin/node
/*
  This script searches the second biggest integer in the list of arguments.
  You can assume all arguments can be converted to integer
  If no argument passed, print 0
  If the number of arguments is 1, print 0
*/
const num = (process.argv.slice(2));

if (num.length < 2) {
  console.log(0);
} else {
  num.sort((a, b) => a - b);
  console.log(parseInt(num[num.length - 2]));
}
