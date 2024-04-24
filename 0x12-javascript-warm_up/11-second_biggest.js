#!/usr/bin/node

const len = process.argv.length - 2;

let secBiggest;

if (len <= 1) {
  secBiggest = 0;
  console.log(secBiggest);
} else {
  const argv = process.argv.slice(2, process.argv.length);
  const newArgv = argv.map(function (num) {
    return Number(num);
  });
  const Biggest = Math.max(...newArgv);
  const withoutBiggest = newArgv.filter(function (num) {
    return num !== Biggest;
  });

  secBiggest = Math.max(...withoutBiggest);
  console.log(secBiggest);
}
