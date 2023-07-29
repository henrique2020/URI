var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
var rep = parseInt(lines.shift());
console.log(Array(rep).fill("Ho").join(" ")+"!");