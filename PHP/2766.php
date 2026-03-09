<?php
// Problema: 2766 - Entrada e Saída Lendo e Pulando Nomes | Resposta: Accepted
// Linguagem: PHP (8.1.2) [+1s]                           | Tempo: 0.000s

for ($i = 1; $i <= 10; $i++) {
    $var = trim(fgets(STDIN));
    if (in_array($i, [3, 7, 9])) {
        echo $var.PHP_EOL;
    }
}
?>