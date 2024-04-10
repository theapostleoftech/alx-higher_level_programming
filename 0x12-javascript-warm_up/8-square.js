#!/usr/bin/node
const Sz = parseInt(process.argv[2]);
if (!+Sz) {
  console.log('Missing size');
} else if (Sz > 0) {
  for (let i = 0; i < Sz; i++) {
    console.log('X'.repeat(Sz));
  }
}
