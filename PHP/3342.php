<?php
// Problema: 3342 - Keanu       | Resposta: Accepted
// Linguagem: PHP (8.1.2) [+1s] | Tempo: 0.127s

$tamanho = intval(fgets(STDIN)) ** 2;
$brancas = ceil($tamanho/2);
$pretas = floor($tamanho/2);

printf("{$brancas} casas brancas e {$pretas} casas pretas\n");
?>
