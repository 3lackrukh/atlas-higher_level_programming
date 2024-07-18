#!/usr/bin/node

if (!isNaN(Number(process.argv[2]))) {
  let i = process.argv[2];
  while (i > 0) {
    let xString = '';
    let k = process.argv[2];
    while (k > 0) {
      xString += 'X';
      k--;
    }
    console.log(`${xString}`);
    i--;
  }
} else {
  console.log('Missing size');
}
