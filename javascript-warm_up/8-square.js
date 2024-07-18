#!/usr/bin/node

if (!isNaN(Number(process.argv[2]))) {
  var i = process.argv[2];
  while (i > 0) {
    xString = '';
    var k = process.argv[2];
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
