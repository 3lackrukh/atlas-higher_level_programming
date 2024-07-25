#!/usr/bin/node

const request = require('request');
const id = '18';
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) throw err;
  const data = JSON.parse(body);
  let count = 0;
  for (const film of data.results) {
    for (const character of film.characters) {
      if (character.includes(id)) {
        count++;
      }
    }
  }
  console.log(count);
});
