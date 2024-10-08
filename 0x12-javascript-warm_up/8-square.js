#!/usr/bin/node
// Write a script that prints x times “C is fun”

const { argv } = require('node:process');
let count = 0;
let message = 'Missing size';
argv.forEach((val, index) => {
  if ((index === 2) && (!isNaN(val))) { count = parseInt(val); }
});
if (count > 0) {
  for (let i = 0; i < count; i++) {
    message = '';
    for (let j = 0; j < count; j++) {
      message += 'X';
    }
    console.log(message);
  }
} else if (count < 0) {
  process.exit(0);
} else { console.log(message); }
