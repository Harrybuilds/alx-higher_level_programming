#!/usr/bin/node

let x = 0;
for (x in process.argv) {
  x++;
}

if (x <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
