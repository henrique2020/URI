<?php
// Problema: 3141 - Dúvida Etária | Resposta: Accepted
// Linguagem: PHP (8.1.2) [+1s]   | Tempo: 0.145s

[$nome, $dt_atual, $dt_nascimento] = [trim(fgets(STDIN)), trim(fgets(STDIN)), trim(fgets(STDIN))];
$dt_atual = DateTime::createFromFormat('d/m/Y', $dt_atual);
$dt_nascimento = DateTime::createFromFormat('d/m/Y', $dt_nascimento);

$anos = $dt_atual->diff($dt_nascimento)->y;

$saida = "";
if($dt_nascimento->format('m-d') == $dt_atual->format('m-d'))
    $saida = "Feliz aniversario!" . PHP_EOL;

$saida .= "Voce tem {$anos} anos {$nome}." . PHP_EOL;
print($saida);
?>