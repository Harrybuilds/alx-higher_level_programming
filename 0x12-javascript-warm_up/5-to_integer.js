#!/usr/bin/node

const len = process.argv.length;

if (len <= 2 || isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(process.argv[2])}`);
}
