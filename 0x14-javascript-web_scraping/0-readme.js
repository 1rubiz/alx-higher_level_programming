#!/usr/bin/node
const filePath = process.argv[2];
const fs = require('fs');

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) { console.log(error); } else { console.log(data); }
});
