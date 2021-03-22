#!/usr/bin/node
/* This script prints My number: <first argument converted in integer>
if the first argument can be converted to an integer print "Not a number" */
const myVar = (process.argv.slice(2));
if (parseInt(myVar[0])) {
  console.log('My number: ' + parseInt(` ${myVar[0]}`));
} else {
  console.log('Not a number');
}
