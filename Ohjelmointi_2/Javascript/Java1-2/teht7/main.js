let maara = Number(prompt('Montako kertaa noppaa heitetään?'));
let summa = 0;
for (let i = 0; i < maara; i++)
{let heitto = Math.floor(Math.random() * 6) +1;
    summa = summa + heitto; }
document.getElementById('tulos').innerHTML = 'Silmälukujen summa: ' + summa;