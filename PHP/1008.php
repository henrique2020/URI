<?php
$id = trim(fgets(STDIN));
$horas = trim(fgets(STDIN));
$valor_hora = trim(fgets(STDIN));

printf("NUMBER = %d\n", $id);
printf("SALARY = U$ %.2f\n", ($horas*$valor_hora));
?>
