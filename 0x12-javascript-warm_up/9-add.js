#!/usr/bin/node
// Write a script that prints two arguments passed to it, in the following format: “ is ”

const { argv } = require('node:process');
let x, y;
argv.forEach((val, index) => {
  if ((index === 2) && (!isNaN(val))) { x = parseInt(val); }
  if ((index === 3) && (!isNaN(val))) { y = parseInt(val); }
});

function add (a, b) { return (a + b); }
const message = add(x, y);
console.log(message);
