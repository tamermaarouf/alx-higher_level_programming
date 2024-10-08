#!/usr/bin/node
const { argv } = require('node:process');

// print process.argv
let total = 0;
argv.forEach((index) => {
  total++;
});
if (total === 3) i{
  console.log('Argument found');
} else if (total > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
