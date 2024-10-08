#!/usr/bin/node
// Write a script that prints two arguments passed to it, in the following format: “ is ”

const { argv } = require('node:process');
let x, y;
argv.forEach((val, index) => {
  if (index === 2) { x = val; }
  if (index === 3) { y = val; }
});
const message = `${x} is ${y}`;
console.log(message);
