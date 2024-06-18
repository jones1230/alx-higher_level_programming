#!/usr/bin/node
const argPos = process.argv[2];
if (typeof argPos === 'undefined') {
  console.log('No argument');
} else {
  console.log(argPos);
}
