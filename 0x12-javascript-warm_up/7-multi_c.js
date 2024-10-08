#!/usr/bin/node
// Write a script that prints x times “C is fun”

const { argv } = require('node:process');
let count = 0;
let message = 'Missing number of occurrences';
argv.forEach((val, index) => {
  if ((index === 2) && (!isNaN(val))) { count = parseInt(val); }
});
if (count > 0) {
  message = 'C is fun';
  for (let i = 0; i < count; i++) {
    console.log(message);
  }
} else if (count < 0) {
  process.exit(0);
} else { console.log(message); }
