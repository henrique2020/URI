<?php
$l = explode(' ', trim(fgets(STDIN)));
$p = $l[0];
$e = $l[1];
$n = $l[2];

$g = $p + $e;
$trocas = 0;
while ($g >= $n) {
    $t = intdiv($g, $n);
    $trocas += $t;

    $g = $g % $n + $t;
}
printf("%d\n", $trocas);
?>