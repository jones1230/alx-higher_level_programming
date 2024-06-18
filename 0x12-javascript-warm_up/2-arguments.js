#!/usr/bin/node
const numOfArg = process.argv.length;
const trueNumOfArg = numOfArg - 2;
if (trueNumOfArg > 0) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
