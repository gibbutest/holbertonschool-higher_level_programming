#!/usr/bin/node

const num = parseInt(process.argv[2]);

// prettier-ignore
function factorial (n) {
  return isNaN(n) || n <= 0 ? 1 : n * factorial(n - 1)
}

console.log(factorial(num));
