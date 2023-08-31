<?php
$bits = explode(" ", trim(fgets(STDIN)));
if(in_array(9, $bits)){ printf("F\n"); }
else { printf("S\n"); }
?>
