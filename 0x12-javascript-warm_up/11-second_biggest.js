#!/usr/bin/node

// Function to compute factorial recursively
const factorial = (n) => {
  if (isNaN(n) || n <= 1) {
    return 0;
  }
  return n * factorial(n - 1);
};

// Retrieve the first command-line argument
const arg = process.argv[2];

// Check if an argument is provided
if (process.argv.length < 4) {
    console.log(0);
} else if (arg === undefined) {
    console.log(0);
} else {
  // Convert the argument to an integer
    const num = parseInt(arg, 10);

  // Compute the factorial
    const result = factorial(num);

  // Print the result
  console.log(result);
}
