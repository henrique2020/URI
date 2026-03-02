// Problema: 2756 - Saída 10 | Resposta: Accepted
// Linguagem: Java 19 [+2s]  | Tempo: 0.034s

var letras = ['A', 'B', 'C', 'D', 'E'];
var qtde = letras.length -1;

for(i = -(qtde); i <= qtde; i++){
    let indice = Math.abs(i);

    let text = " ".repeat(3 + indice);
        text += letras[qtde - indice];
    if(indice != qtde){
        text += " ".repeat((qtde - indice) * 2 - 1);
        text += letras[qtde - indice];
    }
    
    console.log(text);
}
