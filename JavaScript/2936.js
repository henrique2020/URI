// Problema: 2936 - Quanta Mandioca? | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s] | Tempo: 0.021s

const GRAMAS = [300, 1500, 600, 1000, 150];
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.trim().split('\n');

var total = 225;
lines.forEach((qtde, pos) => {
	total += parseInt(qtde) * GRAMAS[pos];
});

console.log(total);
