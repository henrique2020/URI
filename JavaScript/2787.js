var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var n1 = parseInt(lines.shift());
var n2 = parseInt(lines.shift());

if(n1%2 == 0 && n2%2 == 0){
    console.log(1);
} else if (n1%2 != 0 && n2%2 != 0) {
    console.log(1);
} else {
    console.log(0);
}