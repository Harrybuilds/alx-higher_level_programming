#!/usr/bin/node

const lenArgv = process.argv.length - 2;
let args;

if (lenArgv === 0) {
  args = 'No argument';
} else if (lenArgv === 1) {
  args = 'argument found';
} else {
  args = 'Arguments found';
}

console.log(args);
