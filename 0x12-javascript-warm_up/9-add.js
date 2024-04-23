#!/usr/bin/node

const add = function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  console.log(a + b);
};

const len = process.argv.length;
const argv = process.argv;

if (len < 3) {
  console.log('NaN');
} else if (isNaN(argv[2]) || isNaN(argv[3])) {
  console.log('NaN');
} else {
  add(argv[2], argv[3]);
}
