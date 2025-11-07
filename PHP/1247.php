<?php
// Problema: 1247 - Guarda Costeira | Resposta: Accepted
// Linguagem: PHP (8.1.2) [+1s]     | Tempo: 0.000s

define('LIMITE', 12);
while (($linha = fgets(STDIN)) !== false) {
	$valores = array_map('intval', explode(' ', $linha));
	$d = $valores[0];
	$vf = $valores[1]; 
	$vg = $valores[2];
	
	$tf = LIMITE / $vf;
	$tg = sqrt(pow($d, 2) + pow(LIMITE, 2)) / $vg;
	print((($tg <= $tf) ? 'S' : 'N')."\n");
}
?>
