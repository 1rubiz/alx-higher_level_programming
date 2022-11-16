#!/usr/bin/node
/* script that writes a string to a file
- The first argument is the file path
- The second argument is the string to write
- The content of the file must be read in utf-8
If an error occurred during the reading, print the error object */
const args = process.argv;
const fs = require('fs');

fs.readFile(args[2], 'utf-8', (err, data) =>{
  if (error) { console.log(error); } else { console.log(data); }
});
