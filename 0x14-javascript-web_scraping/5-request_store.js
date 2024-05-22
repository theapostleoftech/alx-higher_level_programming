#!/usr/bin/node
// A script to write a web content to file
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
      if (err) {
        console.error('Error writing file:', err);
      }
    });
  }
});
