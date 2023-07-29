var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var phrase = 'LIFE IS NOT A PROBLEM TO BE SOLVED';
var len = parseInt(lines.shift());

console.log(phrase.substring(0, len));