#!/usr/bin/node

const x = process.argv.length;

if (x <= 2 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    let square = '';
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
