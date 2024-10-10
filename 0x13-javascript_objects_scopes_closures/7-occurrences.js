#!/usr/bin/node
/**
 * Write a function that returns the number of occurrences in a list:
 * Prototype: exports.nbOccurences = function (list, searchElement)
 */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const elem of list) {
    if (elem === searchElement) { count++; }
  }
  return count;
};
