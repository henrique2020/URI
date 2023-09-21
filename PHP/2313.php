<?php
$pontos = explode(' ', trim(fgets(STDIN)));
rsort($pontos);
$a = $pontos[0];
$b = $pontos[1];
$c = $pontos[2];

if($a >= ($b+$c)) {
    printf("Invalido\n");
} else {
    if($a == $b && $b == $c) {
        printf("Valido-Equilatero\n");
    } else if ($a == $b || $b == $c || $c == $a) {
        printf("Valido-Isoceles\n");
    } else {
        printf("Valido-Escaleno\n");
    }
    if(($a*$a) == ($b*$b+$c*$c)) {
        printf("Retangulo: S\n");
    } else {
        printf("Retangulo: N\n");
    }
}
?>
