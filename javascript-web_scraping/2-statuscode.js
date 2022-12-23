#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request.get(url, (error, response) => {
  if (!error) console.log(`code: ${response.statusCode}`);
});
