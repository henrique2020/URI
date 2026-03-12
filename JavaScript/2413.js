// Problema: 2413 - Busca na Internet | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s]  | Tempo: 0.030s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
    
console.log(parseInt(lines.shift()) * 4);