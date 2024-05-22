#!/usr/bin/node
// A script that prints all star wars characters

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const movie = JSON.parse(body);
    const charactersUrls = movie.characters;

    const fetchCharacters = charactersUrls.map(url => new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      });
    }));

    Promise.all(fetchCharacters)
      .then(characters => {
        characters.forEach(character => {
          console.log(character.name);
        });
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
});
