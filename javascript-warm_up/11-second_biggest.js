#!/usr/bin/node

const args = process.argv.slice(2);
const nums = args.map(arg => parseInt(arg));

function secondBiggest (nums) {
  let max = Math.max(...nums);
  if (nums.length < 2) {
    console.log(0);
  } else if (nums.indexOf(max) !== -1) {
    nums.splice(nums.indexOf(max), 1);
    max = Math.max(...nums);
    console.log(max);
  }
}

secondBiggest(nums);
