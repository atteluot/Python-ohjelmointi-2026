let nimet = [];
let määrä = Number(prompt("Kuinka monta ossalistuajaa:"))
for (let i = 0; i < määrä; i++) {
  let nimi = prompt('Anna nimi ' + (i + 1) + ':');
  nimet.push(nimi);
}
document.getElementById('tulos').innerHTML = "kaikki nimet:" + nimet;

nimet.sort()

let lista = "";

for (let i = 0;
    i < nimet.length;
     i++) {
  lista = lista + '<li>' + nimet[i] + '</li>';
}
document.getElementById('tulos').innerHTML = '<ol>' + lista + '</ol>';