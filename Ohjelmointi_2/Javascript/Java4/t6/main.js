const form = document.querySelector('form');
const input = document.querySelector('#query');
const results = document.querySelector('#results');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  const value_from_input = input.value;

  fetch(`https://api.chucknorris.io/jokes/search?query=${value_from_input}`)
    .then(function(vastaus) {
      return vastaus.json();
    })
    .then(function(data) {
      results.innerHTML = '';

      data.result.forEach(function(item) {
        const article = document.createElement('article');
        const p = document.createElement('p');
        p.textContent = item.value;
        article.appendChild(p);
        results.appendChild(article);
      });
    });
});