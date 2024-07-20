#!/usr/bin/node

function add (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    const sum = a + b;
    return (sum);
  } else {
    return ('NaN');
  }
}
// export the add function
exports.add = add;
