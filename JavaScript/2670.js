// Problema: 2670 - Máquina de Café  | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s] | Tempo: 0.250s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var [n1, n2, n3] = lines.splice(0,3).map(Number);

var r;
if (n1 + n3 <= 2 * n2) {r = (n1+n3) * 2; }
else if (Math.max(n1, n2, n3) == n1){ r = 2*n2 + 4*n3; }
else if (Math.max(n1, n2, n3) == n3){ r = 4*n1 + 2*n2; }

console.log(r);
