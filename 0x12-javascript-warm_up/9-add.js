#!/usr/bin/node
function add (a, b) {
  a = parseFloat(process.argv[2]);
  b = parseFloat(process.argv[3]);
  const ans = a + b;
  return ans;
}
console.log(add());
