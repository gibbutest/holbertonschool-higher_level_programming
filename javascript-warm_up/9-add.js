#!/usr/bin/node

const { argv } = process;
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

// prettier-ignore
function add (a, b) {
  console.log(a + b);
}

add(a, b);
