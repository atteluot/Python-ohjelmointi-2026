fetch('https://api.chucknorris.io/jokes/random')
  .then(function(vastaus) {
    return vastaus.json();
  })
  .then(function(data) {
    console.log(data.value);
  });