<?php
function valida($pecas, $valores){
    if($valores[0] <= $pecas && $pecas <= $valores[1]){
        return True;
    } else {
        return False;
    }
}

$pecas = trim(fgets(STDIN));
$lavar = explode(' ', trim(fgets(STDIN)));
$secar = explode(' ', trim(fgets(STDIN)));

if(valida($pecas, $lavar) && valida($pecas, $secar)){
    printf("possivel\n");
} else {
    printf("impossivel\n");
}
?>
