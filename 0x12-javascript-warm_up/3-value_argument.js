#!/usr/bin/node
const { argv } = require('node:process');

// print process.argv
let message = 'No argument';
console.log;
argv.forEach((val, index) => {
  if (index === 2) { message = val; }
});

console.log(message);
