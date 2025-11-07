<?php
// Problema: 2936 - Quanta Mandioca? | Resposta: Accepted
// Linguagem: PHP (8.1.2) [+1s]      | Tempo: 0.000s

$gramas = [300, 1500, 600, 1000, 150];

$total = 225;
foreach($gramas as $peso){
	$total += intval(fgets(STDIN)) * $peso;
}

echo "{$total}\n";
?>
