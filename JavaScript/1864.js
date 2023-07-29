var phrase = 'LIFE IS NOT A PROBLEM TO BE SOLVED';
var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
var len = parseInt(lines.shift());

console.log(phrase.substring(0, len));