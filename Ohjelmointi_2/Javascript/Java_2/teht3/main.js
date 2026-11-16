const koirat = [];

for (let i = 0; i < 6; i++) {
  let nimi = prompt('Anna nimi ' + (i + 1) + ':');
  koirat.push(nimi);
}

koirat.sort()
koirat.reverse()

for (let koira of koirat) {
  document.getElementById('tulos').innerHTML += "<li>" + koira + "</li>";
}
