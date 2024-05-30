/*
  this script fetches and replaces name from this URL:
  https://swapi-api.hbtn.io/api/people/5/?format=json
*/
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, function (data, textStatus) {
  $('DIV#character').text(data.name);
});
