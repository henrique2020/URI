// Problema: 1247 - Guarda Costeira  | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s] | Tempo: 0.073s

const LIMITE = 12;
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.trim().split('\n');

lines.forEach(line => {
	let [d, vf, vg] = line.trim().split(' ').map(Number);
	let tf = LIMITE / vf;
	let tg = Math.sqrt(Math.pow(d, 2) + Math.pow(LIMITE, 2)) / vg;
	console.log(tg <= tf ? 'S' : 'N');
});
