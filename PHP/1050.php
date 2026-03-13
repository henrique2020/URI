<?php
// Problema: 1050 - DDD         | Resposta: Accepted
// Linguagem: PHP (8.1.2) [+1s] | Tempo: 0.021s

$DDD = [
    '61' => 'Brasilia',
    '71' => 'Salvador',
    '11' => 'Sao Paulo',
    '21' => 'Rio de Janeiro',
    '32' => 'Juiz de Fora',
    '19' => 'Campinas',
    '27' => 'Vitoria',
    '31' => 'Belo Horizonte'
];

echo ($DDD[trim(fgets(STDIN))] ?? 'DDD nao cadastrado').PHP_EOL;
?>