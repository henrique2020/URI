<?php
// Problema: 2986 - Nem Tudo é Greve Versão Hard | Resposta: Accepted
// Linguagem: PHP (8.1.2) [+1s]                  | Tempo: 0.159s

$MOD = 1000000007;

$N = intval(fgets(STDIN));

if ($N == 0) {
    echo 1 . "\n";
    exit;
}

$dp = array_fill(0, $N+1, 0);
$dp[0] = 1;
if ($N >= 1) $dp[1] = 1;
if ($N >= 2) $dp[2] = 2;
if ($N >= 3) $dp[3] = 4;

for ($i = 4; $i <= $N; $i++) {
    $dp[$i] = ($dp[$i-1] + $dp[$i-2] + $dp[$i-3]) % $MOD;
}

echo $dp[$N] . "\n";

?>
