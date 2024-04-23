#!/usr/bin/node

const x = process.argv.lenght;

if (x < 2 || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const loop = parseInt(process.argv[2]);
  for (let i = 0; i < loop; i++) {
    console.log('C is fun');
  }
}
