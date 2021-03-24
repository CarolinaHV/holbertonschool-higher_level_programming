#!/usr/bin/node
/*
  This function returns the reversed version of a list
*/
exports.esrever = function (list) {
  for (let i = 0; i < list.length / 2; i++) {
  // Swap the elements using destructuring
    [list[i], list[list.length - i - 1]] = [list[list.length - i - 1], list[i]];
  }
  return list;
};
