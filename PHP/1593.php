<?php
// Problema: 1593 - Função Binária | Resposta: Accepted
// Linguagem: PHP (8.1.2) [+1s]    | Tempo: 1.135s

function dividirStringPorDois($numStr) {
    $novoNumero = '';
    $resto = 0;
    $len = strlen($numStr);

    for ($i = 0; $i < $len; $i++) {
        $digito = (int)$numStr[$i];
        $val = ($resto * 10) + $digito;
        $quociente = (int)($val / 2);
        $resto = $val % 2;

        if (!($novoNumero === '' && $quociente === 0)) {
            $novoNumero .= $quociente;
        }
    }
    
    return $novoNumero === '' ? '0' : $novoNumero;
}


$entrada = fopen("php://stdin", "r");
$casos = trim(fgets($entrada));
while ($casos > 0) {
    $n = trim(fgets($entrada));
    if ($n === '') continue;
    
    $qtde_1 = 0;
    while ($n !== '0') {
        $ultimoDigito = (int)substr($n, -1);
        
        if ($ultimoDigito % 2 != 0) {
            $qtde_1++;
        }
        
        $n = dividirStringPorDois($n);
    }
    
    echo $qtde_1 . "\n";
    $casos--;
}

fclose($entrada);
?>
