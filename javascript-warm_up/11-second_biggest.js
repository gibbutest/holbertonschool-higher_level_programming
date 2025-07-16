#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length < 2) {
  console.log(0);
} else {
  const nums = argv.map(Number).sort((a, b) => b - a);
  console.log(nums[1]);
}
