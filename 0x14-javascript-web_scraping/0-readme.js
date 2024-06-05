#!/usr/bin/node

const fs = require('fs').promises;

const readfile = async (filepath) => {
  try {
    const data = await fs.readFile(filepath, 'utf8');
    console.log(data);
  } catch (err) {
    console.error(err);
  }
};

readfile(process.argv[2]);
