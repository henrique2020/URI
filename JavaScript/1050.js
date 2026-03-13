// Problema: 1050 - DDD               | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s]  | Tempo: 0.117s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const DDD = {
    '61': 'Brasilia',
    '71': 'Salvador',
    '11': 'Sao Paulo',
    '21': 'Rio de Janeiro',
    '32': 'Juiz de Fora',
    '19': 'Campinas',
    '27': 'Vitoria',
    '31': 'Belo Horizonte'
};

console.log(DDD[lines.shift()] || 'DDD nao cadastrado');