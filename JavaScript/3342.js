// Problema: 3342 - Keanu            | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s] | Tempo: 0.102s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var tamanho = (parseFloat(lines.shift()) ** 2) / 2;
var [brancas, pretas] = [Math.ceil(tamanho), Math.floor(tamanho)];
console.log(`${brancas} casas brancas e ${pretas} casas pretas`);
