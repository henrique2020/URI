// Problema: 3141 - Dúvida Etária    | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s] | Tempo: 0.041s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.trim().split('\n');

function parseDate(str){
    let [d, m, y] = str.split('/').map(Number);
    return { d, m, y };
}

var nome = lines.shift().trim();

var atual = parseDate(lines.shift());
var nasc = parseDate(lines.shift());

var anos = atual.y - nasc.y;

if (
    atual.m < nasc.m ||
    (atual.m === nasc.m && atual.d < nasc.d)
){
    anos--;
}

if (
    atual.m === nasc.m &&
    atual.d === nasc.d
){
    console.log("Feliz aniversario!");
}

console.log(`Voce tem ${anos} anos ${nome}.`);