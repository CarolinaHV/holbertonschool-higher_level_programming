#!/usr/bin/node
/*
  This script prints x times “C is fun”
  Where x is the first argument of the script
  If the first argument can’t be converted to an integer,
  print “Missing number of occurrences”
*/
const msg = 'C is fun';
const x = (process.argv.slice(2));

if (parseInt(x[0])) {
  for (let i = 0; i < parseInt(x[0]); i++) {
    console.log(`${msg}`);
  }
} else {
  console.log('Missing number of occurrences');
}
