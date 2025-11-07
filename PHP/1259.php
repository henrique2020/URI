<?php
// Problema: 2159 - Número Aproximado de Primos | Resposta: Accepted
// Linguagem: PHP (8.1.2) [+1s]                 | Tempo: 0.022s

$n = intval(fgets(STDIN));
$min = $n / log($n);
$max = 1.25506 * $min;
printf("%.1f %.1f\n", $min, $max);
?>
