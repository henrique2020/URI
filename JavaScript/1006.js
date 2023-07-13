var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var n1 = parseFloat(lines.shift()) * 2;
var n2 = parseFloat(lines.shift()) * 3;
var n3 = parseFloat(lines.shift()) *5;

var media = (n1+n2+n3)/10;
console.log('MEDIA = ' + media.toFixed(1));