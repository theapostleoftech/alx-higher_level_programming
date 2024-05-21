#!/usr/bin/node
// A script to read the contents of a file
const fs = require('fs');

const filePath = process.argv[2];

const readFile = (path) => {
  fs.readFile(path, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
};

if (filePath) {
  readFile(filePath);
} else {
  console.error('Please provide a file path as an argument.');
}
