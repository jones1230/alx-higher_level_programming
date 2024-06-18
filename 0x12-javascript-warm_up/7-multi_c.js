#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing number of occurences');
} else if (arg > 0) {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}
