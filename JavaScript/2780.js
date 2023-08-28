var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var line = input.split('\n');

var d = parseInt(line.shift());
var p;
if (d <= 800) { p = 1; } 
else if (d <= 1400) { p = 2; } 
else { p = 3; }

console.log(p);