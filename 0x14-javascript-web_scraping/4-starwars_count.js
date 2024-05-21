#!/usr/bin/node
// A script that prints the number of movies
// where the character Wedge Antilles is present.

const request = require('request');

function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function countMoviesWithWedgeAntilles (apiUrl) {
  try {
    const data = await fetchData(apiUrl);
    const wedgeAntillesId = 18;
    let count = 0;

    for (const movie of data.results) {
      const characters = await Promise.all(movie.characters.map(fetchData));
      const hasWedgeAntilles = characters.some((character) => character.id === wedgeAntillesId);
      if (hasWedgeAntilles) {
        count++;
      }
    }

    console.log(count);
  } catch (error) {
    console.error('Error:', error);
  }
}

const apiUrl = process.argv[2];

countMoviesWithWedgeAntilles(apiUrl);
