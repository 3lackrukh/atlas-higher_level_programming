#!/usr/bin/node

const myVar = ['No argument', 'Argument found', 'Arguments found'];
const len = process.argv.length;

if (len > 3) {
  console.log(myVar[2]);
} else {
  console.log(myVar[len - 2]);
}
