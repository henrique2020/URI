// Problema: 2766 - Entrada e Saída Lendo e Pulando Nomes | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s]                      | Tempo: 0.048s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

console.log([lines[2], lines[6], lines[8]].join('\n'));