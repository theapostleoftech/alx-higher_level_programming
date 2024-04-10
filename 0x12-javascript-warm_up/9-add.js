#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
let result;
function add (a, b) {
  result = a + b;
  console.log(`${result}`);
}
add(a, b);
