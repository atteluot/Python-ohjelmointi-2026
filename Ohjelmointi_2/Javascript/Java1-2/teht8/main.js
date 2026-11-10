let alku = Number(prompt('Anna alkuvuosi:'));
let loppu = Number(prompt('Anna loppuvuosi:'));
let vuosi = alku;
let lista = '';
while (vuosi <= loppu) {
  if (vuosi % 400 == 0) {
    lista = lista + '<li>' + vuosi + '</li>';} 
    else if (vuosi % 100 == 0) {}
    else if (vuosi % 4 == 0) {
    lista = lista + '<li>' + vuosi + '</li>';}
  vuosi = vuosi + 1;
}
document.getElementById('tulos').innerHTML = '<ul>' + lista + '</ul>';