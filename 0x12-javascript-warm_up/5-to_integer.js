#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(parseFloat(arg))) {
  console.log('Not a number');
} else {
 console.log('My number: ' + parseFloat(arg));
}
