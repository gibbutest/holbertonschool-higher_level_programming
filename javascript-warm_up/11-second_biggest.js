#!/usr/bin/node

const argv = process.argv.slice(2);

if (!argv || argv.length === 1) {
  console.log(0);
} else {
  let big = 0;
  argv.forEach((n) => {
    const num = parseInt(n);
    if (num > big) big = num;
  });
  console.log(big);
}
