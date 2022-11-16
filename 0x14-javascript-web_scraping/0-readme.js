#!/usr/bin/node
/* script that reads and prints the content of a file
- first argument is the file path
- The content of the file must be read in utf-8
- If an error occurred during the reading, print the error object */
const filePath = process.argv[2];
const fs = require('fs');

fs.readFile(filePath, 'utf-8', (error, data)=> {
  if (error) {
    console.log(error);
  } else {
    console.log(data.toString());
  }
});
