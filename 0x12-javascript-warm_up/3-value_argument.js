#!/usr/bin/node
const myArg = process.argv;
myArg.slice(2).forEach((arg, index) => {
  if (!myArg[2]) {
    console.log('No argument');
  } else if (myArg[2]) {
    console.log(`${arg}`);
  }
});

// if (!myArg[2]) {
//     console.log('No argument');
// } else {
//     console.log(`${(myArg[3])}`);
// }
