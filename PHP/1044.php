<?php
// Problema: 1044 - Múltiplos   | Resposta: Accepted
// Linguagem: PHP (8.1.2) [+1s] | Tempo: 0.036s

$num = array_map('intval', explode(" ", fgets(STDIN)));
sort($num);
print(
    ($num[1]%$num[0] == 0 ? "Sao Multiplos" : "Nao sao Multiplos")
    . PHP_EOL
);

?>
