// Problema: 2374 - Pneu             | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s] | Tempo: 0.151s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var [n1, n2] = [
    parseInt(lines.shift()),
    parseInt(lines.shift())
];
console.log(n1-n2)
