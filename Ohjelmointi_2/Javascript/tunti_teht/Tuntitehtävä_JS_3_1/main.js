let nimet = [];

for (let i = 0; i < 5; i++) {
  let nimi = prompt('Anna nimi ' + (i + 1) + ':');
  nimet.push(nimi);
}

document.getElementById('tulos').innerHTML = "kaikki nimet:" + nimet;
document.getElementById('vika').innerHTML = "vika nimi:" + nimet[4];
nimet.sort()
document.getElementById('eka').innerHTML = "eka nimi:" + nimet[0];
document.getElementById('kpe').innerHTML = "Kokolista ilman ekaa:" + nimet[1]+","+nimet[2]+","+nimet[3]+","+nimet[4];