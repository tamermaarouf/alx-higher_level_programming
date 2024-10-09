#!/usr/bin/node
// Write a script that prints x times “C is fun”

const { argv } = require('node:process');
let count = 0;
// const message = 'Missing size';
argv.forEach((val, index) => {
  if (index === 2) { count = val; }
});

function rec (n) {
  if (n <= 1) { return 1; }
  return (n * rec(n - 1));
}
if (isNaN(count)) {
  console.log('1');
} else { console.log(rec(parseInt(count))); }
