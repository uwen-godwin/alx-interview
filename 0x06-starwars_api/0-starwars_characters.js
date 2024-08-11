#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID as an argument.');
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  
  const data = JSON.parse(body);
  const characters = data.characters;
  
  if (!characters) {
    console.log('No characters found for this movie.');
    return;
  }

  // Create an array to store the promises for each character request
  const characterPromises = characters.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  });

  // Wait for all promises to resolve and then print the characters in order
  Promise.all(characterPromises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(err => console.log(err));
});
