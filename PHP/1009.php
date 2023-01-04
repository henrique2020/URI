<?php
trim(fgets(STDIN));
$salario = trim(fgets(STDIN));
$comissao = trim(fgets(STDIN))*0.15;

$valor = $salario + $comissao;
printf("TOTAL = R$ %.2f\n", $valor);
?>
