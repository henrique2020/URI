<?php
$rep = trim(fgets(STDIN));
$ho = [];
for($i = 0; $i < $rep; $i++){ $ho[] = "Ho"; }
print(implode(" ", $ho)."!\n");
?>