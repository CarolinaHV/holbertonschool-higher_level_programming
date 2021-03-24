#!/usr/bin/node
/*
  This function returns the number of occurrences in a list
*/
exports.nbOccurences = function (list, searchElement) {
  const value = list.filter(i => i === searchElement);
  return (value.length);
};
