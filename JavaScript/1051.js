// Problema: 1051 - Imposto de Renda | Resposta: Accepted
// Linguagem: JavaScript 12.18 [+2s] | Tempo: 0.032s

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var valor = parseFloat(lines.shift());

if (valor <= 2000)
    console.log("Isento");
else {
    var imposto = 0;
    let regras = [[4500, 28], [3000, 18], [2000, 8]];
    for (let [vBase, percentual] of regras) {
        if(valor > vBase){
            imposto += (valor - vBase) * percentual / 100;
            valor = vBase;
        }
    }
    console.log("R$", imposto.toFixed(2));
}
