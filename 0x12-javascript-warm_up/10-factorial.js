#!/usr/bin/node

const recur = (num) => {
  num = parseInt(num);
  if (isNaN(num)) {
    return 1;
  }
  if (num <= 1) {
    return num;
  }
  return num + recur(num - 1);
};

console.log(recur(process.argv[2]));
