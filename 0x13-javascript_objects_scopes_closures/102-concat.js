#!/usr/bin/node

const { readFile, writeFile } = require('fs').promises;

const readfile = async function (file) {
  try {
    const fileData = await readFile(file, 'utf-8');
    return fileData;
  } catch (err) {
    console.log(err);
  }
};

const writefile = async function (file, data) {
  try {
    await writeFile(file, data, { flag: 'a' });
  } catch (err) {
    console.log(err);
  }
};

const main = async function () {
  const len = process.argv.length - 2;

  if (len >= 1 && len <= 3) {
    const argv = process.argv.slice(2, process.argv.length);

    const firstFile = await readfile(argv[0]);
    const secondFile = await readFile(argv[1]);
    await writefile(argv[2], firstFile + '\n');
    await writefile(argv[2], secondFile + '\n');
  }
};

main();
