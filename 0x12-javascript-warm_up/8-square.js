#!/usr/bin/node
/*
  This script that prints a square
  The first argument is the size of the square
  If the first argument can’t be converted to an integer, print “Missing size”
  You must use the character X to print the square
*/
const x = (process.argv.slice(2));

if (x.length === 1 && !isNaN(parseInt(x[0]))) {
  for (let i = 0; i < parseInt(x[0]); i++) {
    console.log('X'.repeat(parseInt(x[0])));
  }
} else {
  console.log('Missing size');
}
