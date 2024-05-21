#!/usr/bin/node
// A script that prints the title of
// a Star Wars Movie episode
const request = require('request');

const movieId = process.argv[2];

if (movieId) {
    const api = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

    request(api, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
        } else {
            const movie = JSON.parse(body);

            console.log(movie.title);
        }
    });

} else {
    console.error('Please provide a movie ID as an argument.');
}
