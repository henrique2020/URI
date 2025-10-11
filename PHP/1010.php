<?php
    // Problema: 1010 - Cálculo Simples | Resposta: Accepted
    // Linguagem: PHP (8.1.2) [+1s]     | Tempo: 0.060s

    function arr() {
        return explode(' ', trim(fgets(STDIN)));
    }
    $total = 0;

    $elementos = arr();
    $total += (int) $elementos[1] * (float) $elementos[2];
    $elementos = arr();
    $total += (int) $elementos[1] * (float) $elementos[2];
    
    $total = number_format($total, 2, '.', '');
    print("VALOR A PAGAR: R$ {$total}\n");
?>