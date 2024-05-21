#!/usr/bin/node
// A script that displays
// the status code of a GET request

const request = require('request');

const url = process.argv[2];

if (url) {
  request(url, (error, response) => {
    if (error) {
      console.error('Error:', error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
} else {
  console.error('Please provide a url as an argument.');
}
