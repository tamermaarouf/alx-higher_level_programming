#!/usr/bin/node
// Write a script that prints x times “C is fun”

const { argv } = require('node:process');
let count = 0;
let message = 'Missing number of occurrences';
argv.forEach((val, index) => {
  if ((index === 2) && (!isNaN(val))) { count = parseInt(val); message = 'C is fun'; }
});
if (count > 0) {
  for (let i = 0; i < count; i++) {
    console.log(message);
  }
} else { console.log(message); }
