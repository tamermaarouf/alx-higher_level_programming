#!/usr/bin/node
// Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

const { argv } = require('node:process');
let num = 'Not a number';
argv.forEach((val, index) => {
  if ((index === 2) && (!isNaN(val))) { num = parseInt(val); }
});
const message = `My number: ${num}`;
console.log(message);
