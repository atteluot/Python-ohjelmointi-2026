function noppa() {
    return Math.floor(Math.random()* 6 ) +1;
}

const tulos = document.querySelector("#tulos");

let heitto;
do {
  heitto = noppa();
  tulos.innerHTML += "<li>" + heitto + "</li>";
} while (heitto !== 6);