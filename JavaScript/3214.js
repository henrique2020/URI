var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var line = input.split(' ');

var p = parseInt(line.shift());
var e = parseInt(line.shift());
var n = parseInt(line.shift());

var g = p + e;
var trocas = 0;
while (g >= n) {
    let t = ~~(g/n);    // ~~ cortas os decimais
    trocas += t;
    g = g % n + t;
}
console.log(trocas);