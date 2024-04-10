#!/usr/bin/node
const { argv } = require('node:process');
argv.forEach(index); {
    if (index < 2) {
        console.log('No argument');
    } else if (index === 3) {
        console.log('Argument found');
    } else {
        console.log('Arguments found');
    }

}
