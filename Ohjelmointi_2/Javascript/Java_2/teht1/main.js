let num1 = parseInt(prompt("Anna ensimmäinen luku:"));
let num2 = parseInt(prompt("Anna toinen luku:"));
let num3 = parseInt(prompt("Anna kolmas luku:"));
let num4 = parseInt(prompt("Anna neljäs luku:"));
let num5 = parseInt(prompt("Anna viides luku:"));

let numbers = [num1,num2,num3,num4,num5];

for (let i = numbers.length - 1;
     i >= 0;
      i--) {
        console.log(numbers[i])
      }