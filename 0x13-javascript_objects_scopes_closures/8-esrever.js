#!/usr/bin/node
/**
 * Write a function that returns the reversed version of a list:
 * Prototype: exports.esrever = function (list)
 */

exports.esrever = function (list) {
  const newArray = [];
  let count = 0;
  for (const elem of list) {
    count++;
  }
  for (let j = count; j > 0; j--) {
    newArray.push(list[j - 1]);
  }
  return newArray;
};
