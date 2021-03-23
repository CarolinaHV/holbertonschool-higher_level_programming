#!/usr/bin/node
/*
  This script computes and prints a factorial
  The first argument is integer (argument can be cast as integer) used for computing the factorial
  Factorial of NaN is 1
  You must do it recursively
  You must use a function
*/
function factorial (n) {
  if (n === 1) {
    return 1;
  }
  return (n * factorial(n - 1));
}

const num = (process.argv.slice(2));

if (num[0] === undefined) {
  console.log(1);
} else {
  console.log(factorial(num));
}
