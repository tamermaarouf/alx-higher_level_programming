#!/usr/bin/node
const { argv } = require('node:process');

// print process.argv
let message = 'No argument';
argv.forEach((val, index) => {
  if (index === 2) { message = val; }
});

console.log(message);
