// Problema: 2581 - I am Toorg!      | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s] | Tempo: 0.026s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.trim().split('\n');

(lines.slice(1)).forEach(_ => {
	console.log("I am Toorg!");
});
