// Problema: 1593 - Função Binária   | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s] | Tempo: 0.047s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.trim().split('\n');

lines.shift();
lines.forEach((line)=> {
    binario = BigInt(line).toString(2);
    console.log(binario.split('1').length - 1);
});
