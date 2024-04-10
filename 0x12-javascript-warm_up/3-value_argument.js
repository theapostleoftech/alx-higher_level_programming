#!/usr/bin/node
const myArg = process.argv;
if (myArg[2] === undefined) {
    console.log('No argument');
} else {
    myArg.slice(2).forEach((arg, index) => {
        if (myArg[2]) {
            console.log(`${arg}`);
        }
    });
}
