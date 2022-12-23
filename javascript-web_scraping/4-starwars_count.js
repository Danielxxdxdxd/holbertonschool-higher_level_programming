#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;

request(url, function (error, response, body) {
  if (error) console.log(error);
  const bodyObj = JSON.parse(body).results;
  for (let i = 0; i < bodyObj.length; i++) {
    const charactersList = bodyObj[i].characters;
    for (let j = 0; j < charactersList.length; j++) {
      const characterID = charactersList[j].split('/')[5];
      if (characterID === '18') {
        counter += 1;
      }
    }
  }

  console.log(counter);
});
