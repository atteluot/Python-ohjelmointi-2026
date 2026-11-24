const form = document.querySelector('form');
const input = document.querySelector('#query');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  const value_from_input = input.value;

  fetch(`https://api.tvmaze.com/search/shows?q=${value_from_input}`)
    .then(function(vastaus) {
      return vastaus.json();
    })
    .then(function(data) {
      console.log(data);
    });
});