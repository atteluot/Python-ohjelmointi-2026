let vuosi = Number(prompt('Anna vuosiluku:'));
let teksti = '';

if (vuosi % 400 == 0) {
  teksti = 'Vuosi ' + vuosi + ' on karkausvuosi.';
} else if (vuosi % 100 == 0) {
  teksti = 'Vuosi ' + vuosi + ' ei ole karkausvuosi.';
} else if (vuosi % 4 == 0) {
  teksti = 'Vuosi ' + vuosi + ' on karkausvuosi.';
} else {
  teksti = 'Vuosi ' + vuosi + ' ei ole karkausvuosi.';
}

document.getElementById('tulos').innerHTML = teksti;