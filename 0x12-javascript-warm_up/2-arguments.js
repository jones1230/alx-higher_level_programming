#!/usr/bin/node
const numOfArg = process.argv.length;
const trueNumOfArg = numOfArg - 2;
if (trueNumOfArg === 0) {
  console.log('No argument');
} else if (trueNumOfArg > 0) {
  console.log('Argument found');
};
