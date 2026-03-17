<?php
// Problema: 1120 - Revisão de Contrato | Resposta: Accepted
// Linguagem: PHP (8.1.2) [+1s]         | Tempo: 0.142s

while (true) {
    $input = trim(fgets(STDIN));
    
    if ($input === "0 0" || empty($input)) { break; }

    [$d, $n] = explode(" ", $input);

    $resultado = str_replace($d, "", $n);
    $resultado = ltrim($resultado, "0");

    if ($resultado === "") {
        echo "0\n";
    } else {
        echo $resultado . "\n";
    }
}

?>