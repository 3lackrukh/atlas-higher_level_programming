#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (num) {
  if (num !== 0 && !isNaN(num)) {
    return num * factorial(num - 1);
  } else {
    return 1;
  }
}
console.log(factorial(num));
