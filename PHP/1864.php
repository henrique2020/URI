<?php
$phrase = 'LIFE IS NOT A PROBLEM TO BE SOLVED';
$len = trim(fgets(STDIN));

printf("%s\n", substr($phrase, 0, $len));
?>