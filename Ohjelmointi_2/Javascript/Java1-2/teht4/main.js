'use strict';

const nimi = prompt('Mikä on nimesi?');

const luku = Math.floor(Math.random() * 4) + 1;

let tupa;
if (luku === 1) {
  tupa = 'Rohkelikko';
} else if (luku === 2) {
  tupa = 'Luihuinen';
} else if (luku === 3) {
  tupa = 'Puuskupuh';
} else {
  tupa = 'Korpinkynsi';
}

document.getElementById('tulos').innerHTML = nimi + ', sinä olet ' + tupa + '.';