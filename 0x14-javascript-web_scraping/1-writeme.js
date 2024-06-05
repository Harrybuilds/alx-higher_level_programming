#!/usr/bin/node
const fs = require('fs').promises;

const writefile = async (filepath, content) => {
  try {
    await fs.writeFile(filepath, content, 'utf8', { mode: 'w' });
  } catch (err) {
    console.error(err);
  }
};

const filepath = process.argv[2];
const content = process.argv[3];

writefile(filepath, content);
