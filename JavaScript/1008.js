var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var n = parseInt(lines.shift());
var h = parseInt(lines.shift());
var s = parseFloat(lines.shift());

console.log('NUMBER = ' + n);
console.log('SALARY = U$ ' + (h*s).toFixed(2));