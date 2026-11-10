let teksti = '';
let haluaa = confirm('Lasketaanko neliöjuuri?');

if (haluaa == true) {
  let luku = Number(prompt('Anna luku:'));

  if (luku < 0) {
    teksti = 'Negatiivisen luvun neliöjuurta ei ole määritelty.';
  } else {
    let juuri = Math.sqrt(luku);
    teksti = 'Luvun ' + luku + ' neliöjuuri on ' + juuri;
  }
} else {
  teksti = 'Neliöjuurta ei lasketa.';
}

document.getElementById('tulos').innerHTML = teksti;