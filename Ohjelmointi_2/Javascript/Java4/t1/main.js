const form = document.querySelector('form');
const input = document.querySelector('#query');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  const haku = input.value;
  const osoite = 'https://api.tvmaze.com/search/shows?q=' + haku;

  fetch(osoite)
    .then(function(vastaus) {
      return vastaus.json();
    })
    .then(function(data) {
      console.log(data);
    });
});