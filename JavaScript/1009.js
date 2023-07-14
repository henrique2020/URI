var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var nome = lines.shift();
var slario = parseFloat(lines.shift());
var vendas = parseFloat(lines.shift());

var salario_total = slario + (vendas*0.15);
console.log('TOTAL = R$ ' + salario_total.toFixed(2));