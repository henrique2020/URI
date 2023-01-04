var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
    
var a = parseFloat(lines.shift());
a = (a*3.5)/10;
var b = parseFloat(lines.shift());
b = (b*7.5)/10;

var media = ((a+b)*10)/11;
   
console.log('MEDIA = ' + media.toFixed(5));
