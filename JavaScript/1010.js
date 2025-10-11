// Problema: 1010 - Cálculo Simples  | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s] | Tempo: 0.024s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.trim().split('\n');

var total = 0;
lines.forEach(line => {
    let dados = line.split(' ');
    total += parseInt(dados[1]) * parseFloat(dados[2]);
});

console.log(`VALOR A PAGAR: R$ ${total.toFixed(2)}`);