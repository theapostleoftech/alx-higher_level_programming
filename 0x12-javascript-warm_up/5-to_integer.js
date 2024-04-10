#!/usr/bin/node
const myArg = process.argv;
let myNumber;
myArg.slice(2).forEach((arg, index) => {
  if ((myArg === undefined) || (!+arg)) {
    console.log('Not a number');
  } else {
    myNumber = (+arg);
    console.log(`My number: ${myNumber}`);
  }
});
