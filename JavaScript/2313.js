var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var pontos = input.split(' ');
pontos.sort(function(a, b){return a - b});
pontos.reverse();

var a = parseInt(pontos[0]);
var b = parseInt(pontos[1]);
var c = parseInt(pontos[2]);

if(a >= (b+c)) {
    console.log('Invalido')
} else {
    if(a == b && b == c) {
        console.log('Valido-Equilatero');
    } else if (a == b || b == c || c == a) {
        console.log('Valido-Isoceles');
    } else {
        console.log('Valido-Escaleno');
    }
    if((a*a) == (b*b+c*c)) {
        console.log('Retangulo: S');
    } else {
        console.log('Retangulo: N');
    }
}