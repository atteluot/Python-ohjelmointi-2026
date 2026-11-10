
let luku1 = parseInt(prompt("Anna ensimmäinen kokonaisluku:"), 10);
let luku2 = parseInt(prompt("Anna toinen kokonaisluku:"), 10);
let luku3 = parseInt(prompt("Anna kolmas kokonaisluku:"), 10);

let summa = luku1 + luku2 + luku3;
let tulo = luku1 * luku2 * luku3;
let keskiarvo = summa / 3;

document.getElementById("summa").textContent = "Lukujen summa: " + summa;
document.getElementById("tulo").textContent = "Lukujen tulo: " + tulo;
document.getElementById("keskiarvo").textContent = "Lukujen keskiarvo: " + keskiarvo;
