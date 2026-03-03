// Problema: 1044 - Múltiplos        | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s] | Tempo: 0.030s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var nums = lines.shift().trim().split(' ').map(Number);
nums.sort((a, b) => a - b);

console.log(nums[1] % nums[0] === 0 ? "Sao Multiplos" : "Nao sao Multiplos");
