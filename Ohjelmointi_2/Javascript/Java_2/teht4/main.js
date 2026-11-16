const numerot = [];
let luku = Number(prompt("Anna numero (0 lopettaa):"));

while (luku !== 0) {
  numerot.push(luku);
  luku = Number(prompt("Anna numero (0=stop):"));
}

numerot.sort((a, b) => b - a)


for (let numero of numerot) {
  document.getElementById('tulos').innerHTML += "<li>" + numero + "</li>";
}



