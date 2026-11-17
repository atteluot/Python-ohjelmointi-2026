const numbers = [];

while (true) {
  const num = Number(prompt("Anna numero:"));

  if (numbers.includes(num)) {
    console.log("Numero " + num + " on jo annettu.");
    break;
  }

  numbers.push(num);
}

numbers.sort((a, b) => a - b);
console.log(numbers);
for (const number of numbers) {
  tulos.innerHTML += "<li>" + number + "</li>";
}