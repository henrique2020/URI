// Problema: 2159 - Número Aproximado de Primosa | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s]             | Tempo: 0.036s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var line = input.trim();

let n = parseInt(line);
let min = n / Math.log(n);
let max = 1.25506*min;
console.log(min.toFixed(1), max.toFixed(1));
