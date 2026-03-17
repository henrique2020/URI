// Problema: 1120 - Revisão de Contrato | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s]    | Tempo: 0.080s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.trim().split('\n');

for (let line of lines) {
    const parts = line.trim().split(' ');
    
    if (parts.length < 2) continue;
    
    const [D, N] = parts;
    if (D === '0' && N === '0') break;

    const regex = new RegExp(D, 'g');
    let resultado = N.replace(regex, '');
    resultado = resultado.replace(/^0+/, '');

    if (resultado === "") { console.log("0"); }
    else {console.log(resultado); }
}