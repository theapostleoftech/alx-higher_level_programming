#!/usr/bin/node
const n = parseInt(process.argv[2]);
let result;
function factorial (n) {
  if (!+n) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
result = factorial(n);
console.log(result);
